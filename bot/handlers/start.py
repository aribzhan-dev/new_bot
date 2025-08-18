from aiogram import Router, types
from aiogram.filters import CommandStart
from bot.keyboards.common import main_keyboard

router = Router()

@router.message(CommandStart())
async def on_start(msg: types.Message):
    await msg.answer(
        "Salom! Botga hush kelibsiz.",
        reply_markup=main_keyboard()
    )