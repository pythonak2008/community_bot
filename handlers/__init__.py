from aiogram import Router
from .user import router as users_router
from .group import router as group_router

router = Router()

router.include_routers(users_router)
router.include_router(group_router)
