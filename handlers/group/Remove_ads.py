import asyncio
from aiogram.types import Message, ChatPermissions
from aiogram.enums import ChatType
from aiogram import Router, F
from data.config import Adwords, links, GROUPS_
from keyboards.inline.menu import link_bot
from loader import bot
from datetime import datetime, timedelta

router = Router()
Black_List = {}


@router.message(F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}))
async def handle_antispam(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    ads = Adwords + links

    await message.answer("🤖 Ushbu bot faqat belgilangan guruhlarda faol.", reply_markup=link_bot)
    try:
        if message.text and any(word in message.text.lower() for word in ads):
            await message.delete()
            print(f"🚫 Reklama aniqlandi: {user_id}")

            if user_id in Black_List:
                attempts = Black_List[user_id].get("attempts", 0) + 1
                Black_List[user_id]["attempts"] = attempts

                if attempts >= 3:
                    until_date = datetime.now() + timedelta(minutes=1)
                    await bot.restrict_chat_member(
                        chat_id=chat_id,
                        user_id=user_id,
                        permissions=ChatPermissions(can_send_messages=False),
                        until_date=until_date
                    )
                    await message.answer(
                        "🚷 Siz 3 marta man etilgan soz yozdingiz.\n"
                        "1 daqiqa davomida xabar yuborish cheklab qoyildi.\n"
                        f"👤 USER: @{message.from_user.username if message.from_user.username else message.from_user.first_name}"
                    )
                else:
                    left_attempts = 3 - attempts
                    await message.answer(
                        f"⚠️ Siz {attempts} marta ruxsat etilmagan soz kiritdingiz.\n"
                        f"Yana {left_attempts} imkoniyatingiz bor ‼️"
                    )
            else:
                Black_List[user_id] = {
                    "first_name": message.from_user.first_name,
                    "last_name": message.from_user.last_name or "",
                    "until_date": 0,
                    "status": "goodboy",
                    "attempts": 1
                }
    except Exception as e:
        pass

    if message.new_chat_members:
        for new_user in message.new_chat_members:
            await message.answer(f"Xush kelibsiz, {new_user.full_name}!")
            await message.delete()

    elif message.left_chat_member:
        user = message.left_chat_member
        await message.answer(f"{user.full_name} groupdan chiqdi.")
        await message.delete()



