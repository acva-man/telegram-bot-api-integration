from aiohttp import web
from aiogram import Bot, types
from .config import settings
from .bot import create_bot, create_dispatcher
from .di import DIContainer

async def handle_webhook(request):
    """Handle incoming Telegram webhook updates"""
    bot = request.app['bot']
    dispatcher = request.app['dispatcher']
    
    update = types.Update(**await request.json())
    await dispatcher.process_update(update)
    
    return web.Response()

async def on_startup(app):
    """Configure webhook on application startup"""
    bot = app['bot']
    await bot.set_webhook(f"{settings.WEBHOOK_URL}{settings.WEBHOOK_PATH}")

async def init_app():
    """Initialize application with dependencies"""
    app = web.Application()
    
    # Initialize DI container
    di_container = DIContainer()
    app['di_container'] = di_container
    
    # Initialize bot and dispatcher
    bot = await create_bot()
    dispatcher = await create_dispatcher(bot, di_container)
    
    app['bot'] = bot
    app['dispatcher'] = dispatcher
    
    app.router.add_post(settings.WEBHOOK_PATH, handle_webhook)
    app.on_startup.append(on_startup)
    
    return app

if __name__ == "__main__":
    web.run_app(init_app(), host=settings.SERVER_HOST, port=settings.SERVER_PORT)
