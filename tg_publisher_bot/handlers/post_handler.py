from aiogram import Router, F, types
from aiogram.fsm.context import ContextTypes
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config.settings import config
from services.publisher import publish_to_channel

router = Router()

@router.message(F.text | F.photo)
async def handle_new_post(message: types.Message, state: ContextTypes.FSMContext):
    # Сохраняем данные во временное хранилище (FSM)
    await state.update_data(
        content_text=message.text or message.caption,
        photo=message.photo if message.photo else None
    )
    
    # Создаем кнопки с выбором каналов
    builder = InlineKeyboardBuilder()
    for name, channel_id in config.CHANNELS.items():
        builder.button(text=f"Опубликовать в {name}", callback_data=f"pub_{channel_id}")
    
    await message.answer("Контент получен. Куда постим?", reply_markup=builder.as_markup())

@router.callback_query(F.data.startswith("pub_"))
async def process_publish(callback: types.CallbackQuery, state: ContextTypes.FSMContext):
    channel_id = int(callback.data.split("_")[1])
    data = await state.get_data()
    
    # Логика отправки
    await publish_to_channel(
        bot=callback.bot,
        channel_id=channel_id,
        message_data={"text": data.get("content_text"), "photo": data.get("photo"), "caption": data.get("content_text")}
    )
    
    await callback.answer("Опубликовано!")
    await callback.message.edit_text(f"✅ Пост отправлен в канал (ID: {channel_id})")
    await state.clear()