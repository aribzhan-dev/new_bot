import asyncio
from aiogram import Bot, Dispatcher
from config import TELEGRAM_TOKEN
from bot.handlers.start import router as start_router
from bot.handlers.proverbs import router as proverbs_router
from bot.models.base import init_engine
from bot.handlers.password import router as password_router
from bot.handlers.hash_pass import router as hash_handler
from bot.handlers.iin import router as iin_router
from bot.services.scheduler import start_scheduler
from bot.handlers.task import router as task_router

async def main():
    await init_engine()
    start_scheduler()

    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(proverbs_router)
    dp.include_router(password_router)
    dp.include_router(hash_handler)
    dp.include_router(iin_router)
    dp.include_router(task_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())