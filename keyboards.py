from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Кнопка на главной
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(KeyboardButton("Узнать свою версию"))

# Вопрос пользователю
answers_kb = ReplyKeyboardMarkup(resize_keyboard=True)
answers_kb.add(
    KeyboardButton("☕ Кофе"),
    KeyboardButton("💻 Работа"),
    KeyboardButton("️ Сон")
)
