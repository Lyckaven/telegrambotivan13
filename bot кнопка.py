from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = '6209915591:AAFSmfW1yRU9zjFV9eZU0y0RtGw2NzuEzlU'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаем список с кнопками
buttons: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(8)]

# Распаковываем список с кнопками в билдер, указываем, что
# в одном ряду должно быть 3 кнопки
kb_builder.row(*buttons, width=3)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=kb_builder.as_markup(
                                            resize_keyboard=True))

if __name__ == '__main__':
    dp.run_polling(bot)