from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.enums import ChatType
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from data.config import group_rules
from keyboards.inline.service_menu import get_button
from loader import  db
from keyboards.default.menu import get_phone_number_btn, info_bot, back_button
from states.ExampleState import ExampleState
from datetime import datetime

router = Router()

@router.message(F.text == '📝 Royxatan otish')
async def full_name1(message: Message, state: FSMContext):
    await message.answer('👤 Ismingizi kiriting', reply_markup=back_button)
    await state.set_state(ExampleState.full_name)
    await message.delete()


@router.message(StateFilter(ExampleState.full_name))
async def last_name1(message: Message, state: FSMContext):
    if message.text == '⬅️ Ortga':
        await message.answer("Ortga qaytildingiz", reply_markup=await get_button())
        await message.delete()
        return
    await state.update_data(full_name=message.text)
    await message.answer('👤 Familiyangizi kiriting', reply_markup=back_button)
    await state.set_state(ExampleState.last_name)
    await message.delete()


@router.message(StateFilter(ExampleState.last_name))
async def age_1(message: Message, state: FSMContext):
    if message.text == '⬅️ Ortga':
        await message.answer("👤 Ismingizi kiriting", reply_markup=back_button)
        await state.set_state(ExampleState.full_name)
        await message.delete()
        return
    await state.update_data(last_name=message.text)
    await message.answer('📆 Yoshingizi kiriting\n'
                         'Misol: 23.07.2008', reply_markup=back_button)
    await state.set_state(ExampleState.age)
    await message.delete()


@router.message(StateFilter(ExampleState.age))
async def get_city(message: Message, state: FSMContext):
    if message.text == '⬅️ Ortga':
        await message.answer("👤 Familiyangizi kiriting", reply_markup=back_button)
        await state.set_state(ExampleState.last_name)
        await message.delete()
        return
    try:
        born_date = datetime.strptime(message.text, "%d.%m.%Y")
        await state.update_data(age=message.text)
        await message.answer("📲 Telefon raqamingizni kiriting", reply_markup=get_phone_number_btn)
        await state.set_state(ExampleState.phone_number)
        await message.delete()
    except ValueError:
        await message.answer("❌ Format notogri.\n"
                             "Misol: 23.07.2008")
        await message.delete()


@router.message(StateFilter(ExampleState.phone_number), F.contact)
async def finish_state(message: Message, state: FSMContext):
    user_id1 = message.from_user.id
    phone_number = message.contact.phone_number

    data = await state.get_data()
    full_name = data.get('full_name')
    last_name = data.get('last_name')
    age = data.get('age')

    await db.insert_some_information_of_user(
        full_name=full_name,
        last_name=last_name,
        age=age,
        phone_number=phone_number,
        user_id=user_id1
    )
    await message.answer('✅ Royxatan otingiz', reply_markup=ReplyKeyboardRemove())
    await state.set_state(ExampleState.next)
    await message.answer(text=group_rules, reply_markup=await get_button())
    await state.clear()





