from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject

class InjectBotMiddleware(BaseMiddleware):
    def __init__(self, bot: Bot):
        self.bot = bot

    async def __call__(self, handler, event: TelegramObject, data: dict):
        data["bot"] = self.bot
        return await handler(event, data)
