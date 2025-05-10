from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def register_start__inline_btn():
    menu = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Sign Up", callback_data='register')
        ]
    ])
    return menu
