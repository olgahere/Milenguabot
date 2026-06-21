"""
Минимальный бот для запуска Mini App "Italiano Tetris".

УСТАНОВКА:
    pip install aiogram --break-system-packages   (или просто pip install aiogram)

НАСТРОЙКА:
    1. Вставь свой токен в BOT_TOKEN ниже (или задай переменную окружения BOT_TOKEN)
    2. После деплоя фронтенда на Vercel вставь URL в WEBAPP_URL
    3. Запусти: python bot.py

ЗАПУСК НА ХОСТИНГЕ (чтобы бот работал 24/7, не на твоём компьютере):
    Можно бесплатно задеплоить на Railway.app или Render.com (Background Worker).
    Для самого первого теста — достаточно запустить локально на своём компьютере.
"""

import asyncio
import os
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN", "8573031484:AAEIcp3mWr6HXWt1J90cMsQACkLU8a899gg")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://milenguabot.vercel.app")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text="🎮 Играть и учить итальянский",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        ]]
    )
    await message.answer(
        "Ciao! 🇮🇹\n\n"
        "Это игра-тренажёр итальянского языка в стиле Tetris.\n"
        "Лови правильные переводы падающих слов, набирай очки "
        "и постепенно прокачивайся от A1 до B2.\n\n"
        "Жми кнопку ниже, чтобы начать первый раунд (5 слов, ~5 минут):",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
