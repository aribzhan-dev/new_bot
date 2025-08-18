from aiogram import Router, types, F
from bot.keyboards.common import LABEL_MAQOL
from bot.services.proverbs import fetch_random_proverb  # yoki fetch_all_proverbs

router = Router()

@router.message(F.text == LABEL_MAQOL)
async def send_random_proverb(msg: types.Message):
    proverb = await fetch_random_proverb()
    if not proverb:
        await msg.answer("Maqollar topilmadi. (DB bo‘sh)")
        return
    await msg.answer(f"📜 {proverb}")