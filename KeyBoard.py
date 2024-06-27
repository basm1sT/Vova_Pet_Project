from aiogram.types import(
    InlineKeyboardButton, InlineKeyboardMarkup,
    KeyboardButton,ReplyKeyboardRemove, ReplyKeyboardMarkup, WebAppInfo)

from aiogram.utils.keyboard import(InlineKeyboardBuilder, KeyboardBuilder, ReplyKeyboardBuilder)
from aiogram.filters.callback_data import CallbackData

from config import TG_CHANEL_URL


link_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Tellegram Chanel', url=TG_CHANEL_URL)
    ]
])

admin_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Пользователи, прошедшие через бота', callback_data='active_users'),
        InlineKeyboardButton(text='Смешной кот', callback_data='funny_cat')
    ]
])