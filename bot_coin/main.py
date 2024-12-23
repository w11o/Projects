from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import random
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, WebAppData, ReplyKeyboardMarkup, KeyboardButton, ContentType
from aiogram import F
from aiogram.filters import Filter
import types
from typing import Union, Dict, Any

API_TOKEN = ''

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
kb_builder = ReplyKeyboardBuilder()

web_app_button = KeyboardButton(
    text="Открыть веб-приложение",
    web_app=WebAppInfo(url='https://w11o.github.io/test/')
)

kb_builder.row(web_app_button, width=1)

keyboard_app: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)


def draw_hexagram(hexagram):
    hexagram_lines = []
    for line in hexagram:
        if line == 1:
            hexagram_lines.append("——")  # Целая линия
        else:
            hexagram_lines.append("— —")  # Прерванная линия
    
    # Формируем итоговую гексаграмму с нужным форматированием
    return "\n".join(hexagram_lines)
hexagram = [1, 0, 1, 1, 0, 1]
hexagram_drawn = draw_hexagram(hexagram)

# Команда старт
@dp.message(CommandStart())
async def send_welcome(message: Message):
        await message.reply(
        """<b>Привет, <i>дружище!</i> 🌟</b>
        
        Я — <b>бот для подбрасывания монеты</b>, и я готов помочь тебе сделать выбор. 📍
        
        Просто нажми кнопку, чтобы бросить монету, и я покажу результат!

        <b>Инструкция:</b>
        <i>/flip</i> — чтобы подбросить монету
        <i>/hex</i> — чтобы нарисовать гексаграмму
        <i>/start</i> — чтобы увидеть приветственное сообщение

        Я работаю для тебя 24/7! 💪""",
        parse_mode=ParseMode.HTML
    )
        await bot.send_photo(
        message.chat.id,
        "https://anashina.com/wp-content/uploads/2019/03/Zhou-yi.jpg",  # Замените на актуальную ссылку
        caption="Канон Перемен (И-цзин)"  # Подпись к изображению
    )

        await message.answer(
            text='эта кнопка будет открывать веб-приложение',
            reply_markup=keyboard_app
            )
    

# Команда подбросить монетку
@dp.message(Command(commands=["flip"]))
async def flip_coin(message: Message):
    # Рандомный выбор орел или решка
    result = random.choice(['Орел', 'Решка'])
    
    # Отправляем результат с использованием HTML
    await message.reply(
        f"<b>Результат подбрасывания монетки:</b>\n\n<b>{result}</b>",

    )

 
open_menu_button = InlineKeyboardButton(
    text='Открыть меню',
    callback_data='open_menu_button_pressed'
)


@dp.callback_query(F.data == 'open_menu_button_pressed')
async def open_menu_button_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text= """<b>Привет, <i>дружище!</i> 🌟</b>
        
        Я — <b>бот для подбрасывания монеты</b>, и я готов помочь тебе сделать выбор. 📍
        
        Просто нажми кнопку, чтобы бросить монету, и я покажу результат!

        <b>Инструкция:</b>
        <i>/flip</i> — чтобы подбросить монету
        <i>/hex</i> — чтобы нарисовать гексаграмму
        <i>/start</i> — чтобы увидеть приветственное сообщение

        Я работаю для тебя 24/7! 💪""",
        parse_mode=ParseMode.HTML,
        reply_markup=callback.message.reply_markup
    )

    
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[open_menu_button]]
)



@dp.message(Command(commands=["hex"]))
async def send_echo(message: Message):
        await message.reply(
        f"<pre>{hexagram_drawn}</pre>",
        parse_mode=ParseMode.HTML
    )



@dp.message(F.content_type == ContentType.WEB_APP_DATA)
async def handle_web_app_data(message: Message):
    
    print(message.web_app_data)
    print(message.from_user.id)
    print(message.from_user.first_name)
    print(message.from_user.last_name)
    print(message.from_user.username)
    print(message.from_user.language_code)
    await message.answer("Received web app data")




@dp.message()
async def send_echo(message: Message):
        print(f'{message.from_user.id}: {message.text}')
        await message.reply(
        "Напишите /start чтобы увидеть инструкцию!", reply_markup=keyboard)






if __name__ == '__main__':
    dp.run_polling(bot)

