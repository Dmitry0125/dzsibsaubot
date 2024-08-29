from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from lexicon.lexicon_ru import LEXICON_RU

# Создаем объекты инлайн-кнопок
big_button_1 = InlineKeyboardButton(
    text='Сайт СибГУ',
    url='https://www.sibsau.ru/'
)

big_button_2 = InlineKeyboardButton(
    text='Репозиторий на GitHub этого проекта',
    url='https://github.com/Dmitry0125/dzsibsaubot'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2]]
)