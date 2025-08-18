from sqlalchemy import text
from datetime import datetime, date, time as dtime
from dateutil import tz
from bot.models.base import get_session
from bot.services.scheduler import plan_job

TZ = tz.gettz("Asia/Almaty")
MY_TIMEZONE = datetime.now(tz=TZ).astimezone(TZ)
MY_CHAT_ID = 123456789

def parse_time_string(s: str) -> datetime:
    s = s.strip()
    # 1) Absolyut vaqt: 2025-08-20 18:30
    try:
        dt = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
        return dt.replace(tzinfo=TZ)
    except ValueError:
        pass
    # 2) bugungi vaqt

    try:
        t =  datetime.strptime(s, "%Y-%m-%d")
        today = date.today()
        return datetime.combine(today, t).replace(tzinfo=TZ)
    except ValueError:
        pass

    raise ValueError("Kutilgan fromatlar : %Y-%m-%d %H:%M:%S yoki %H:%M:%S")


async def insert_task(title: str, description: str, run_at: datetime) -> int:
    async with get_session() as session:
        result = await session.execute(
            text("""
                INSERT INTO task (title, description, "time", is_done)
                VALUES (:title, :description, :time, FALSE)
                RETURNING id
            """),
            {"title": title, "description": description, "time": run_at.astimezone(tz.UTC)}
        )
        task_id = result.scalar_one()
        await session.commit()
        return task_id

async def create_task_and_schedule(title: str, description: str, time_str: str) -> int:
    run_at_local = parse_time_string(time_str)
    task_id = await insert_task(title, description, run_at_local)
    await plan_job(task_id, run_at_local)
    return task_id
