import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.settings import config
from handlers import post_handler

async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_router(post_handler.router)
    
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())