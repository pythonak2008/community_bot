from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router()

registration = ReplyKeyboardMarkup(keyboard=[
    [
    KeyboardButton(text='📝 Royxatan otish')
    ],
],
    resize_keyboard=True
)

get_phone_number_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Raqamni yuborish", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


info_bot = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Botni malumoti")
    ],
],
    resize_keyboard=True

)

back_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Ortga')
        ],
    ],
    resize_keyboard=True
)
