import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import json

bot = telebot.TeleBot('7779383986:AAFRgqsNHLLcC3N1MU8EHhNEJ3XAZ055jBg')

with open('books.json', encoding='utf-8') as file:
    books = json.load(file)
with open('users.json', encoding='utf-8') as file:
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
    bot.send_message(message.chat.id,
                     "*👋 Hi, this is an app for searching for books at your discretion.*\n /start - to start bot\n /info - information of the bot",
                     reply_markup=markup, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "search_book":
        send_random_book(call.message)
    elif call.data == "further":
        send_random_book(call.message)
    elif call.data.startswith("add_book_"):
        book_id = call.data.split("_", 2)[-1]
        add_book(call, book_id)
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
        callback_data=f"add_book_{ran_index}"
    ))
    markup.add(InlineKeyboardButton(
        text="Further",
        callback_data="further"
    ))
    markup.add(InlineKeyboardButton(
        text="Stop Search",
        callback_data="stop"
    ))
    bot.send_message(message.chat.id,
                     f"*📚 New Book for you:*\n* - Name:* {name}\n* - Author:* {author}\n* - Year:* {year}\n* - Genre:* {genre}",
                     reply_markup=markup, parse_mode="Markdown")


def add_book(call, book_id):
    book_info = books["books"][book_id]

    user_id = call.from_user.id

    if str(user_id) not in users:
        users[str(user_id)] = []

    users[str(user_id)].append(book_info)

    with open('users.json', 'w', encoding='utf-8') as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

    bot.answer_callback_query(call.id, "Book added to your list!")


def telegram_channel(call):
    bot.send_message(call.message.chat.id,
                     "<b><a href='t.me/+CqXQeFrb11EyZjQy'>Telegram</a></b>",
                     parse_mode="HTML")


bot.infinity_polling()
