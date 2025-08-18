import typing as t
from sqlalchemy import text
from bot.models.base import get_session



async def fetch_random_proverb() -> str | None:
    """
    PostgreSQL-da eng samarali random: ORDER BY RANDOM() LIMIT 1
    """
    async with get_session() as session:
        result = await session.execute(text("SELECT proverbb FROM proverb ORDER BY RANDOM() LIMIT 1"))
        row = result.first()
        print(row)
        return row[0] if row else None

async def fetch_all_proverbs() -> t.List[str]:
    async with get_session() as session:
        result = await session.execute(text("SELECT proverbb FROM proverb"))
        print(result)
        return [r[0] for r in result.fetchall()]