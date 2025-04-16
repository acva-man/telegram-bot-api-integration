from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from ..services.api_service import APIService
from ..services.data_service import DataService
from ..repositories.postgres import PostgresRepository
from ..repositories.google_sheets import GoogleSheetsRepository

def register_handlers(dp: Dispatcher, di_container):
    dp.register_message_handler(
        cmd_start, 
        commands=['start'], 
        state="*"
    )
    dp.register_callback_query_handler(
        handle_get_users, 
        lambda c: c.data == 'get_users'
    )

async def cmd_start(message: types.Message):
    """Обработчик команды /start с инлайн-кнопками"""
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        text="Получить пользователей", 
        callback_data="get_users"
    ))
    
    await message.answer(
        "Выберите действие:", 
        reply_markup=keyboard
    )

async def handle_get_users(callback: types.CallbackQuery, state: FSMContext):
    """Обработчик получения пользователей из API"""
    try:
        api_service = APIService(di_container.http_client)
        users = await api_service.get_users()
        
        data_service = DataService(
            di_container.postgres_repo,
            di_container.google_sheets_repo
        )
        await data_service.save_users(users)
        
        await callback.message.answer("Данные успешно сохранены!")
    except Exception as e:
        await callback.message.answer(f"Ошибка: {str(e)}")
    finally:
        await callback.answer()
