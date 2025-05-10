from aiogram import Router,F
from aiogram.types import CallbackQuery

from data.config import group_rules
from handlers.user.registration import full_name1
from keyboards.default.menu import registration
from keyboards.inline.menu import ads_btn
from keyboards.inline.service_menu import get_button
from loader import db,dp
from aiogram.types import Message


router = Router()
text = """<b>
1) added Groups
--------------
2) Add Groups
</b>
"""


@router.callback_query(F.data == 'rule_1')
async def rule1(call:CallbackQuery):
    menu = 0
    for i in await  db.users_12(call.from_user.id):
        print(i['group_id'])
        menu += 1
    await call.message.answer(text=text,reply_markup=await ads_btn(menu))
    await call.message.delete()


@router.callback_query(F.data == 'back')
async def back_handler(call: CallbackQuery):
    await call.message.answer(text=group_rules, reply_markup=await get_button())
    await call.message.delete()


@router.callback_query(F.data == 'rule_2')
async def back_handler(call: CallbackQuery):
    await call.message.answer(text=await full_name1(),reply_markup=await full_name1())


