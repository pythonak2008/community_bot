from aiogram import Router
from .start import router as users_start
from .registration import router as users_registration
from .remove_ads_panel import router as users_ads_

router = Router()

router.include_routers(users_start,users_registration)
router.include_router(users_ads_)

