from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

async def get_button():
    menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Reklama Tarqatilmasligi", callback_data='rule_1')],
        [InlineKeyboardButton(text="Bot Orqali Ro'yxatdan O'tish", callback_data='rule_2')],
        [InlineKeyboardButton(text="Kirdi-chiqdilarni Tozalash", callback_data='rule_3')]
    ])
    return menu


