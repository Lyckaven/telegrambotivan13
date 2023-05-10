from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = '6209915591:AAFSmfW1yRU9zjFV9eZU0y0RtGw2NzuEzlU'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Создаем объекты кнопок
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаем первый список с кнопками
buttons_1: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(8)]

# Распаковываем список с кнопками методом add
kb_builder.add(*buttons_1)

# Явно сообщаем билдеру сколько хотим видеть кнопок в 1-м и 2-м рядах
kb_builder.adjust(1, 3)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=kb_builder.as_markup(
                                            resize_keyboard=True))

@dp.message(Text(text='Кнопка 1'))
async def process_dog_answer(message: Message):
    await message.answer(text='Но вы видели как они боятся огурцов?',
                         reply_markup=ReplyKeyboardRemove())


@dp.message(Text(text='Кнопка 2'))
async def process_cat_answer(message: Message):
    await message.answer(text=' вы видели как они боятся огурцов?',
                         reply_markup=ReplyKeyboardRemove())


if __name__ == '__main__':
    dp.run_polling(bot)