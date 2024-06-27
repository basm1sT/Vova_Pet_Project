from aiogram import Router, F, Bot
from aiogram.types import Message, Sticker, CallbackQuery
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.methods import DeleteMessage
from aiogram.exceptions import TelegramBadRequest

import sqlite3

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from contextlib import suppress

from config import *

from KeyBoard import link_kb, admin_kb


class User(StatesGroup):
    idef = ()
    username = ()

bot = Bot(BOT_TOKEN)

rt = Router()

@rt.message(CommandStart())
async def start_cmd(message: Message, state: FSMContext):

    connection = sqlite3.connect('129database.db')
    cursor = connection.cursor()

    await message.answer(text=f'Привет, {message.from_user.first_name}, я пришел тебя заскамить :)')
    await message.answer_sticker(STICKER_ID)
    await message.answer(text='Этот бот не многое умеет, но он <b>ОЧЕНЬ</b> полезен, в оссобенности для Гоги Волева, '
                         'так-что быстрее прейите в его тг канал и станьте лучшей версией себя!', parse_mode='HTML',
                         reply_markup=link_kb)
    try: cursor.execute('INSERT INTO Users (id, username) VALUES (?, ?)', (message.from_user.id, message.from_user.username))
    except: pass
    await bot.send_message(chat_id=CHAT_ID, text=f'Новый типчик!\nUsername: @{message.from_user.username}')
    cursor.execute('SELECT username FROM Users')

    connection.commit()

@rt.message(Command('admin_help'))
async def admin_help_cmd(message: Message):

    if message.from_user.username=='itssteech':
        await message.answer(text='Ой, вова, не ожидал вас здесь увидеть! Вот ваши возможности:', reply_markup=admin_kb)

@rt.callback_query(F.data)
async def callback_cmd(callback: CallbackQuery):

    data = callback.data

    connection = sqlite3.connect('129database.db')
    cursor = connection.cursor()

    if data == 'active_users':
        USERS = ''
        cursor.execute('SELECT username FROM Users')
        users = cursor.fetchall()

        for user in users:
            for i in user:
                USERS = USERS + i + ' '

        await bot.send_message(chat_id=CHAT_ID, text=USERS)

    elif data == 'funny_cat':
        await callback.message.reply_sticker('CAACAgIAAxkBAAEMYiNmfQvu9yLNXauwXrJSuhq3oLVM5QACjQADI1wKCK02JqA3hhxiNQQ')

    connection.close()
