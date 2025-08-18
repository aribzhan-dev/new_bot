from aiogram import Router, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from bot.services.iin import check_iin
from bot.keyboards.common import LABEL_IIN


router = Router()


class IINStates(StatesGroup):
    waiting_for_iin = State()

#1) iin buttoni bosilgandan keyin iin soraymiz
@router.message(F.text == LABEL_IIN)
async def ask_iin(msg: types.Message, state: FSMContext):
    await msg.answer("Iltimos IIN kiriting !!")
    await state.set_state(IINStates.waiting_for_iin)

# 2) Foydalanuvchi yuborgan parolni qabul qilib, hash qilib qaytaramiz
@router.message(IINStates.waiting_for_iin, F.text)
async def process_iin(msg: types.Message, state: FSMContext):
    iin = msg.text
    checked_iin = check_iin(iin)
    await msg.answer(f"IIN tekchirildi : {checked_iin} !!")
    await state.clear()

