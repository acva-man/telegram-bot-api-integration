from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from .di import DIContainer
from .handlers import register_handlers
from .config import settings

async def create_bot() -> Bot:
    """Create and configure Telegram bot instance"""
    bot = Bot(token=settings.TELEGRAM_TOKEN)
    return bot

async def create_dispatcher(bot: Bot, di_container: DIContainer) -> Dispatcher:
    """Create and configure dispatcher with handlers"""
    storage = MemoryStorage()
    dispatcher = Dispatcher(bot, storage=storage)
    
    register_handlers(dispatcher, di_container)
    
    return dispatcher
