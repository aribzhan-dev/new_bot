from aiogram import Router, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from bot.keyboards.common import LABEL_TASK
from bot.services.task import create_task_and_schedule

router = Router()

class TaskStates(StatesGroup):
    waiting_title = State()
    waiting_description = State()
    waiting_time = State()

@router.message(F.text == LABEL_TASK)
async def ask_title(msg: types.Message, state: FSMContext):
    await msg.answer(f"📝 Task sarlavhasini kiriting (title):")
    await state.set_state(TaskStates.waiting_title)

@router.message(TaskStates.waiting_title, F.text)
async def receive_title(msg: types.Message, state: FSMContext):
    await state.update_data(title=msg.text.strip())
    await msg.answer(f"✍️ Task descriptionini kiriting (description):")
    await state.set_state(TaskStates.waiting_description)

@router.message(TaskStates.waiting_description, F.text)
async def receive_desc(msg: types.Message, state: FSMContext):
    await state.update_data(description=msg.text.strip())
    await msg.answer(f" ⏰ Vaqtni kiriting (masalan: 2025-08-20 18:30:00 yoki 18:30:00 bugun):")
    await state.set_state(TaskStates.waiting_time)

@router.message(TaskStates.waiting_time, F.text)
async def receive_time(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    title = data["title"]
    description = data["description"]
    time_str = msg.text.strip()


    try:
        task_id = await create_task_and_schedule(
            title=title,
            description=description,
            time_str=time_str,
        )
    except ValueError as e:
        await msg.answer(f"❌ Vaqt formati xato: {e}\nQayta kiriting, masalan: 2025-08-20 18:30:00 yoki 18:30:00 bugun:")
        return

    await msg.answer(f"✅ Task saqlandi (id={task_id}). Belgilangan vaqtda eslatma yuboraman.")
    await state.clear()
