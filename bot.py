# -*- coding: utf-8 -*-
import os
import telebot
import cloudinary
import cloudinary.uploader
import cloudinary.utils
import cloudinary.api
import time

# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
# some_api_token = os.environ['SOME_API_TOKEN']
#             ...

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...

BOT = telebot.TeleBot(token)
updates = BOT.get_updates()
startDate
cloudinary.config(
    cloud_name="eu-sep",
    api_key="511481921314569",
    api_secret="ERbXpHjdMlU91qcBEslQCY5ReyE"
)


def upload(photo):
    cloudinary.uploader.upload(
        "https://api.telegram.org/file/bot" + token + "/" +
        BOT.get_file(photo.photo[-1].file_id).file_path)


photo_array = ['https://avatars3.githubusercontent.com/u/10268386?s=400&u=c22979fe17a17df6aa32d3cf7326e8370160dd47&v=4',
               'https://avatars1.githubusercontent.com/u/4401928?s=400&v=4']

photo_array = ['https://avatars3.githubusercontent.com/u/10268386?s=400&u=c22979fe17a17df6aa32d3cf7326e8370160dd47&v=4',
               'https://avatars1.githubusercontent.com/u/4401928?s=400&v=4']

    print(message)
    upload(message)


def upload_picture(message):
    print(message)
    upload(message)
    BOT.reply_to(
        message, "Please use the attach image button instead of attaching a document")


@BOT.message_handler(content_types=['document'])
def user_uploads_document(message):
    upload(photo)

        message, "Please use the attach image button instead of attaching a document")


    BOT.reply_to(message, "Testing 123")

def user_uploads_photo(photo):
    upload(photo)

    for url in photo_array:
        BOT.send_message(
            message.chat.id, "[Options](" + url + ")", parse_mode = "Markdown")

def send_welcome(message):
    BOT.reply_to(message, "Testing 123")


@BOT.message_handler(func = lambda message: True)
def echo_all(message):
    for url in photo_array:
        BOT.send_message(
            message.chat.id, "[Options](" + url + ")", parse_mode = "Markdown")


BOT.polling()
