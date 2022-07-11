from pprint import pprint

from aiogram import types
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import logging


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Салам алейкум {message.from_user.full_name}")

@dp.message_handler(commands=['meme'])
async def meme_handler(message: types.Message):
    photo = open('media/123.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)

@dp.message_handler(commands=['quiz'])
async def quiz_handler(message: types.Message):
    murkup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Next', callback_data='button_call_1')
    murkup.add(button_call_1)
    question = "За сколько хочешь меня купить?"
    answers = ["15к сом", "10 сом", "Бесплатно"]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type ='quiz',
        correct_option_id=2,
        explanation='Размечтался Не продаюсь',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=murkup,


    )

@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    murkup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Next', callback_data='button_call_2')
    murkup.add(button_call_2)
    question = "Кто создал Python ?"
    answers = ["Эди Мерфи", "Чарли Чаплин", "Черный дракон"]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Ну давай сам',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=murkup,

    )
@dp.callback_query_handler(lambda call: call.data == 'button_call_2')
async def quiz_3(call: types.CallbackQuery):
    question = "Кто создал Python ?"
    answers = ["Эди Мерфи", "Чарли Чаплин", "Черный дракон"]
    photo = open('media/123.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Ну давай сам',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        i = message.text
        await bot.send_message(message.from_user.id, f'{int(i)*int(i)}')
    else:
        await bot.send_message(message.from_user.id, message.text)

if __name__ == "__main__":
     logging.basicConfig(level=logging.INFO)
     executor.start_polling(dp, skip_updates=True)

#
# await bot.send_message(message.from_user.id,
#                            f"Салам алейкум {message.from_user.full_name}")