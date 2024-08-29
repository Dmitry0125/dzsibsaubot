from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_tomorrow = KeyboardButton(text=LEXICON_RU['tomorrow'])
button_another_date = KeyboardButton(text=LEXICON_RU['another_date'])
button_donate = KeyboardButton(text=LEXICON_RU['donate'])
button_schedule = KeyboardButton(text=LEXICON_RU['schedule'])

# Инициализируем билдер для клавиатуры
start = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
start.row(button_tomorrow, button_another_date, button_donate, button_schedule, width=2)

# Создаем клавиатуру с кнопками
start: ReplyKeyboardMarkup = start.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)