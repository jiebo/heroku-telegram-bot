# -*- coding: utf-8 -*-
"""Telegram bot"""
import os
import time
import urllib

import cloudinary
import cloudinary.api
import cloudinary.uploader
import cloudinary.utils
import telebot

CONST_TEMP_IMAGE_FILE_NAME = "temp.jpg"

TOKEN = os.environ['TELEGRAM_TOKEN']
BOT = telebot.TeleBot(TOKEN)
TEST_ID = int(0)
cloudinary.config(
    cloud_name="eu-sep",
    api_key="511481921314569",
    api_secret="ERbXpHjdMlU91qcBEslQCY5ReyE"
)
USER_IMAGE_DICTIONARY = {}


def upload(url):
    """Uploads user-uploaded image onto Cloudinary"""
    cloudinary.uploader.upload(
        url,
        use_filename=True,
        unique_filename=True)


PHOTO_ARRAY = [
    'https://avatars3.githubusercontent.com/u/10268386?u=c22979fe17a17df6aa32d3cf7326e8370160dd47'
]


@BOT.message_handler(content_types=['photo'])
def user_uploads_photo(photo):
    """When user uploads an image"""
    filename = BOT.get_file(photo.photo[-1].file_id).file_path
    url = "https://api.telegram.org/file/bot" + TOKEN + "/" + filename
    username = photo.from_user.username

    if username not in USER_IMAGE_DICTIONARY:
        BOT.reply_to(photo, "Use /create_test so that we know these images belong to you")
    else:
        USER_IMAGE_DICTIONARY[photo.from_user.username].append(url)
        print(USER_IMAGE_DICTIONARY)


@BOT.message_handler(content_types=['document'])
def user_uploads_document(message):
    """When user uses the wrong upload button"""
    BOT.reply_to(
        message, "Please use the attach image button instead of attaching a document")


@BOT.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Default command"""
    BOT.reply_to(message, "Use /create_test to start")


@BOT.message_handler(commands=['create_test'])
def send_welcome(message):
    """Return the Test ID and create a directory in Cloudinary"""
    USER_IMAGE_DICTIONARY[message.chat.username] = [0]
    BOT.reply_to(message, "Proceed to upload your images, " +
                 "and call /start_test in your target chat group after you are done")


@BOT.message_handler(commands=['start_test'])
def start_test(message):
    """Retrieve images from Cloudinary and save to photo array"""
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)

    for idx, url in enumerate(PHOTO_ARRAY):
        downloadImageFile(url)
        photo = open(CONST_TEMP_IMAGE_FILE_NAME, 'rb')
        BOT.send_photo(message.chat.id, photo, '/Option' + str(idx + 1))
        option_btn = telebot.types.KeyboardButton("Option " + str(idx + 1))
        markup.add(option_btn)

    BOT.send_message(message.chat.id, "Which is the best?", reply_markup=markup)


def downloadImageFile(url):
    """Download image from URL and save into temp file"""
    f = open(CONST_TEMP_IMAGE_FILE_NAME, 'wb')
    f.write(urllib.request.urlopen(url).read())
    f.close()


BOT.polling()
