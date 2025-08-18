from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

LABEL_MAQOL = "Maqol"
LABEL_PASSWORD = "Password"
LABEL_HASH = "Hash"
LABEL_IIN = "IIN"
LABEL_TASK = "Task"

def main_keyboard() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text=LABEL_MAQOL), KeyboardButton(text=LABEL_PASSWORD)],
        [KeyboardButton(text=LABEL_HASH), KeyboardButton(text=LABEL_IIN),],
        [KeyboardButton(text=LABEL_TASK)]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Tugmani tanlang"
    )

