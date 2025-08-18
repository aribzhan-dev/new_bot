from aiogram import Router, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from bot.services.hash_pass import hash_password
from bot.keyboards.common import LABEL_HASH

router = Router()

class HashStates(StatesGroup):
    waiting_for_password = State()

# 1) "Hash" tugmasi bosilganda parol so'raymiz
@router.message(F.text == LABEL_HASH)
async def ask_password(msg: types.Message, state: FSMContext):
    await msg.answer("🔑 Iltimos, parol kiriting:")
    await state.set_state(HashStates.waiting_for_password)

# 2) Foydalanuvchi yuborgan parolni qabul qilib, hash qilib qaytaramiz
@router.message(HashStates.waiting_for_password, F.text)
async def process_password(msg: types.Message, state: FSMContext):
    password = msg.text
    hashed = hash_password(password)
    # HTML code blokda yuborish — maxsus belgilar muammosini oldini oladi
    await msg.answer(f"Hashlangan parol:\n<code>{hashed}</code>", parse_mode="HTML")
    await state.clear()

# 3) Qo'shimcha: /hash <parol> ko'rinishidagi tez buyruq
@router.message(F.text.startswith("/hash"))
async def hash_handler(msg: types.Message):
    parts = msg.text.split(maxsplit=1)
    if len(parts) < 2:
        await msg.answer("❌ Parol kiriting: /hash <parol>")
        return
    password = parts[1]
    hashed = hash_password(password)
    await msg.answer(f"🔑 Hashlangan parol:\n<code>{hashed}</code>", parse_mode="HTML")