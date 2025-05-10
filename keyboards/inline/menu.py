from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message
from data.config import BOT_USERNAME


def get_main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔗 Link", url="https://t.me/yourchannel")],
        [InlineKeyboardButton(text="📞 Contact", callback_data="contact_support")]
    ])


link_bot = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Click me", url='https://t.me/bot_username'.format(bot_username=BOT_USERNAME))
    ]
])


info_bot = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Botni malumoti",callback_data='bot_info')
    ]
])

async def ads_btn(number):
    if not number:
        menu = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text='2)  Qoshish + ', callback_data='add')
            ],
            [
                InlineKeyboardButton(text='⬅️ Ortga', callback_data='back')
            ]
        ])
    else:
        menu = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f'1)   {f"Groups: {number}" if number > 1 else "Group"}',callback_data='groups'
                ),
                InlineKeyboardButton(text='2)  Add + ', callback_data='add')
            ],
            [
                InlineKeyboardButton(text='⬅️ Ortga', callback_data='back')
            ]
        ])
    return menu

