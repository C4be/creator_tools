from aiogram import Bot

async def publish_to_channel(bot: Bot, channel_id: int, message_data: dict):
    """
    Универсальная функция для пересылки или копирования контента.
    """
    if message_data.get("photo"):
        await bot.send_photo(
            chat_id=channel_id,
            photo=message_data["photo"][-1].file_id,
            caption=message_data.get("caption")
        )
    elif message_data.get("text"):
        await bot.send_message(
            chat_id=channel_id,
            text=message_data["text"]
        )
    # Можно расширить для видео, документов и т.д.