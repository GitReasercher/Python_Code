import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Вставьте сюда ваш токен от BotFather
API_TOKEN = '7575252657:AAG_TB4Y2D4kX2IUbtUp_cWUcFxwCLd-it4'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработка команды /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я твой первый бот на Python.")

# Эхо-режим: бот отвечает тем же текстом, что прислал пользователь
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())