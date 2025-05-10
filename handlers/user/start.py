from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.default.menu import registration
from keyboards.inline.register_buttons import register_start__inline_btn
from loader import dp, bot, db
router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message,state:FSMContext):
    await message.answer("Assalomu Alaykum xush kelibsiz.\n"
                         "Royxatan otish uchun pastagi tugmani bosing ⬇️",reply_markup=registration)
    await db.make_user(message.from_user.id)
    await state.clear()
    print(message.from_user.id)
