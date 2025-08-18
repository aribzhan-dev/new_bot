from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy import text
from aiogram import Bot
from datetime import datetime
from dateutil import tz
from bot.models.base import get_session
from config import TELEGRAM_TOKEN, MY_CHAT_ID

scheduler = AsyncIOScheduler()
TZ = tz.gettz("Asia/Almaty")
MY_TIMEZONE = datetime.now(tz=TZ).astimezone(TZ)

from config import TELEGRAM_TOKEN, MY_CHAT_ID

async def notify_task(task_id: int):
    async with get_session() as session:
        row = (await session.execute(
            text("SELECT title, description, is_done FROM task WHERE id = :id"),
            {"id": task_id}
        )).first()
        if not row:
            return
        title, description, is_done = row
        if is_done:
            return

        bot = Bot(token=TELEGRAM_TOKEN)
        try:
            await bot.send_message(MY_CHAT_ID, f"⏰ Eslatma!\n<b>{title}</b>\n{description}", parse_mode="HTML")
        finally:
            await bot.session.close()

        await session.execute(text("UPDATE task SET is_done = TRUE WHERE id = :id"), {"id": task_id})
        await session.commit()

async def plan_job(task_id: int, run_at_local: datetime):
    scheduler.add_job(
        notify_task,
        "date",
        run_date=run_at_local,
        args=[task_id],
        id=f"task_{task_id}",
        replace_existing=True,
        timezone=TZ,
    )

def start_scheduler():
    if not scheduler.running:
        scheduler.start()