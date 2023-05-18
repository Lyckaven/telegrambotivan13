from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = '6209915591:AAFSmfW1yRU9zjFV9eZU0y0RtGw2NzuEzlU'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()


buttons_1: list[KeyboardButton] = [KeyboardButton(
                text=f'начало ') for i in range(1)]


buttons_2: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(1)]


buttons_3: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(1)]


buttons_4: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(1)]


buttons_5: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(1)]


buttons_6: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(1)]


buttons_7: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(1)]


buttons_8: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(1)]


buttons_9: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(1)]


buttons_10: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(1)]


kb_builder.add(*buttons_1)


kb_builder.add(*buttons_2)


kb_builder.add(*buttons_3)


kb_builder.add(*buttons_4)


kb_builder.add(*buttons_4)


kb_builder.add(*buttons_5)


kb_builder.add(*buttons_6)


kb_builder.add(*buttons_7)


kb_builder.add(*buttons_8)


kb_builder.add(*buttons_9)


kb_builder.add(*buttons_10)


kb_builder.adjust(1, 3)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=kb_builder.as_markup(
                                            resize_keyboard=True))


@dp.message(Text(text='Начало'))
async def process_dog_answer(message: Message):
    await message.answer(text='Да, несомненно, кошки боятся собак. '
                              'Но вы видели как они боятся огурцов?')


@dp.message(Text(text=''))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов ')


@dp.message(Text(text=''))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов ')


@dp.message(Text(text=''))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов ')


@dp.message(Text(text=''))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов ')


@dp.message(Text(text=''))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов ')


@dp.message(Text(text=''))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов ')


@dp.message(Text(text=''))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов ')


@dp.message(Text(text=''))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов ')


@dp.message(Text(text=''))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов ')


if name == 'main':
        dp.run_polling(bot)