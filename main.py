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


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id,
                     f"""*Creator:* @mkkamozin\n*Date of first creation:* 6 march 2025\n*Project Description: * The project was created with the support of the educational institution "Kemerovo Talent Center". This bot will help find a book in the user's favorite genres.""",
                     parse_mode="Markdown")


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
    elif call.data == "profile":
        profile(call)


def send_random_book(message):
    ran_index = random.choice(list(books["books"].keys()))
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
        text="My Profile",
        callback_data="profile"
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


def profile(call):
    user_id = str(call.from_user.id)
    user_name = f"{call.from_user.first_name} {call.from_user.last_name}"
    message_text = f"*👤 Your Profile:*\n* - User name:* {user_name}\n* - Favorite books:*\n"

    if user_id in users and users[user_id]:
        books_list = "\n".join([f"📖 {book['name']} by {book['author']} ({book['year']}). Genre is {book['genre']}" for book in users[user_id]])
        message_text += books_list
    else:
        message_text += "You have no favorite books yet."

    bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown")


bot.infinity_polling()
