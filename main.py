import asyncio
from loader import dp, bot, db
from middleares.inject_bot import InjectBotMiddleware
from handlers import router as handler_router


import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

async def main():



    dp.message.middleware(InjectBotMiddleware(bot))
    dp.include_router(handler_router)


    # connect with database
    await db.conf()



    await db.create_groups_table()
    await db.create_register_list_table()
    await db.create_clear_table()
    await db.create_remove_ads_table()


    # make user table:
    await db.make_user_database()


    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
