from aiogram import Router, types, F
from bot.keyboards.common import LABEL_PASSWORD
from bot.services.password import generate_password


router = Router()


@router.message(F.text == LABEL_PASSWORD)
async def password(msg: types.Message):
    pwd = generate_password(8)
    await msg.answer(f"🔐 Parol: `{pwd}`", parse_mode="Markdown")
