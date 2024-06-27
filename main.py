from aiogram import Bot, Dispatcher

from config import *
from hendlers import rt

import asyncio
HTML='HTML'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

dp.include_router(rt)



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print('Exit')