import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

WEBAPP_URL = "https://example.com"  # потом заменим на реальный

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(
        text="🎁 Открыть магазин NFT подарков",
        web_app=types.WebAppInfo(url=WEBAPP_URL)
    ))
    await message.answer(
        "Привет! Добро пожаловать в магазин NFT подарков 🎁\nНажми кнопку чтобы открыть каталог:",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
