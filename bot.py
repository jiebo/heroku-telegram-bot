# -*- coding: utf-8 -*-
import redis
import os
import telebot
from cloudinary_manager import upload
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
#some_api_token = os.environ['SOME_API_TOKEN']
#             ...

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...

bot = telebot.TeleBot(token)
updates = bot.get_updates()
print(updates)

@bot.message_handler(commands=['upload'])
def upload_picture(message):
  upload()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Testing 123")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
