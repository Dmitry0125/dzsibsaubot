from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

from keyboards.start_kb import start
from keyboards.help_kb import keyboard

# Инициализируем роутер уровня модуля
router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=start)

# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=keyboard)

# Этот хэндлер срабатывает на приветствие бота
@router.message(F.text.lower() == LEXICON_RU['hi'])
async def process_yes_answer(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

# Этот хэндлер срабатывает на сообщение "Как дела?"
@router.message(F.text.lower() == LEXICON_RU['how_are_you'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['how_are_you_from_bot'])

# Этот хэндлер срабатывает на просьбу сообщить id
@router.message(F.text.lower() == LEXICON_RU['id'])
async def process_yes_answer(message: Message):
    await message.answer(f'Your ID: {message.from_user.id}')

# Этот хэндлер срабатывает на благодарность боту
@router.message(F.text.lower() == LEXICON_RU['thanks'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['thanks_from_bot'])

# Этот хендлер срабатывает на нажатие кнопки "Донат"
@router.message(F.text == LEXICON_RU['donate'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['donate_from_bot'])

