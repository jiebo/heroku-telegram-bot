# -*- coding: utf-8 -*-
import redis
import os
import telebot
import cloudinary
import cloudinary.uploader
import cloudinary.utils
import cloudinary.api
from telebot import types

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
cloudinary.config(
  cloud_name = "eu-sep", 
  api_key = "511481921314569", 
  api_secret = "ERbXpHjdMlU91qcBEslQCY5ReyE" 
)

def upload():
  cloudinary.uploader.upload("https://vignette.wikia.nocookie.net/youtubepoop/images/f/f7/5Pikachu.png/revision/latest?cb=20141108062013")

photo_array = [ 'https://avatars3.githubusercontent.com/u/10268386?s=400&u=c22979fe17a17df6aa32d3cf7326e8370160dd47&v=4', 'https://avatars1.githubusercontent.com/u/4401928?s=400&v=4' ]


@bot.message_handler(commands=['upload'])
def upload_picture(message):
  upload()

@bot.message_handler(content_types=['document', 'image'])
def user_uploads_photo(message):
  print("received a new photo")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Testing 123")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  for p in photo_array:
    bot.send_message(message.chat.id, p)

bot.polling()
