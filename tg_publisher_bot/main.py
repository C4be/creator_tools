import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.settings import config
from handlers import msg_from_channel_router, post_router


async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_router(msg_from_channel_router)
    dp.include_router(post_router)
    
    
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())