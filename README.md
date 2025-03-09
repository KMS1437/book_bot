# Book Bot

## Overview

Book Bot is a Telegram bot designed to help users discover books based on their preferred genres. The bot presents books in a swipeable feed format, allowing users to browse through various titles and select ones they might like to read.

**Note:** Currently, the database in JSON format does not include book descriptions or cover images, but these features are planned for future updates.

## Features

- **Swipeable Feed:** The bot presents books in a feed format, making it easy to browse through multiple titles.
- **Simple Interface:** Easy-to-use commands and interactions within Telegram.

## How to Use

1. **Insert Your Token:**
   - Open `main.py` and replace `'token'` with your actual Telegram bot token:
     ```python
     bot = telebot.TeleBot('your_token_here')
     ```

2. **Install Required Libraries:**
   - Ensure you have all the necessary libraries installed by running:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Bot:**
   - Start the bot by executing:
     ```bash
     python main.py
     ```

## Telegram Bot Tag

You can find and interact with the bot on Telegram using the following tag:
- **@books_for_moods_bot**
  

## Future Plans

- **Add Book Descriptions and Cover Images:** Enhance the database to include detailed descriptions and cover images for each book.
- **Add a genre selection feature:** Users choose their tastes and books are found only at their sight

---

**Current Version:** 0.4
**Last Updated:** March 9, 2025
