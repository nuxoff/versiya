import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from keyboards import start_kb, answers_kb
from gpt import generate_version_text

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Я помогу узнать, какая ты сейчас версия себя. Готов?",
        reply_markup=start_kb
    )

@dp.message_handler(lambda message: message.text == "Узнать свою версию")
async def ask_question(message: types.Message):
    await message.answer("Окей, начнём! Что тебе ближе по утрам?", reply_markup=answers_kb)

@dp.message_handler(lambda message: message.text in ["☕ Кофе", "💻 Работа", "️ Сон"])
async def show_version(message: types.Message):
    user_choice = message.text
    await message.answer("Генерирую твою версию... Жди немного.")
    result = await generate_version_text(user_choice)
    await message.answer(result, reply_markup=start_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
