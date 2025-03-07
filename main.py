import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import sqlite3
import pandas

bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        text="Start searhing for books",
        callback_data="search_book"
    ))
    markup.add(InlineKeyboardButton(
        text="Telegram-channel of Developer",
        callback_data="telegram_channel"
    ))
    bot.send_message(message.chat.id, "Hi, this is app for searching for books at your discretion", reply_markup=markup)


@bot.message_handler(func=lambda call: True)
def search_book(call):
    if call.data == "search_book":
        ...

def add_book(call):
    if call.data == "add_book":
        ...

def telegram_channel(call):
    if call.data == "telegram_channel":
        bot.send_message(message.chat.id,
                         "<b><a href='t.me/+CqXQeFrb11EyZjQy'>Telegram</a></b>",
                         parse_mode="HTML")

bot.infinity_polling()
