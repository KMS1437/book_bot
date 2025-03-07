import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import sqlite3
import pandas

bot = telebot.TeleBot('7779383986:AAHc4ZKIk3vMpK15jwD2N4JfeUivZp3S1yY')


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        text="Начать искать книги",
        callback_data="search_book"
    ))
    markup.add(InlineKeyboardButton(
        text="Telegram канал разработчика",
        callback_data="telegram_channel"
    ))
    bot.send_message(message.chat.id, "Привет, это приложение для форса книг на твое усмотрение", reply_markup=markup)


@bot.message_handler(func=lambda call: True)
def add_book(call):
    if call.data == "add_book":
        ...

def search_book(call):
    if call.data == "search_book":
        ...

def telegram_channel(call):
    if call.data == "telegram_channel":
        bot.send_message(bot.chat.id, "")

bot.infinity_polling()