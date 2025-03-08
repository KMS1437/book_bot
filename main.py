import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import json

bot = telebot.TeleBot('token')

with open('books.json') as file:
    books = json.load(file)
with open('users.json') as file:
    users = json.load(file)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        text="Start searching for books",
        callback_data="search_book"
    ))
    markup.add(InlineKeyboardButton(
        text="Telegram-channel of Developer",
        callback_data="telegram_channel"
    ))
    bot.send_message(message.chat.id, "Hi, this is an app for searching for books at your discretion.",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "search_book":
        send_random_book(call.message)
    elif call.data == "further":
        send_random_book(call.message)
    elif call.data == "add_book":
        add_book(call)
        send_random_book(call.message)
    elif call.data == "telegram_channel":
        telegram_channel(call)


def send_random_book(message):
    ran_index = str(random.randint(1, len(books["books"])))
    book_info = books["books"][ran_index]
    name = book_info['name']
    author = book_info['author']
    year = book_info['year']
    genre = book_info['genre']

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        text="Add book",
        callback_data="add_book"
    ))
    markup.add(InlineKeyboardButton(
        text="Further",
        callback_data="further"
    ))
    markup.add(InlineKeyboardButton(
        text="Stop Search",
        callback_data="stop"
    ))
    bot.send_message(message.chat.id, f"Name: {name}\nAuthor: {author}\nYear: {year}\nGenre: {genre}",
                     reply_markup=markup)


def add_book(call):
    bot.answer_callback_query(call.id, "Book added to your list!")
    ...


def telegram_channel(call):
    bot.send_message(call.message.chat.id,
                     "<b><a href='t.me/+CqXQeFrb11EyZjQy'>Telegram</a></b>",
                     parse_mode="HTML")


bot.infinity_polling()
