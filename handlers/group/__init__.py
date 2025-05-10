from .Remove_ads import router as group_router

from aiogram import Router


router = Router()
# router.include_routers(group_router,user_router)
router.include_router(group_router)
