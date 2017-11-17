# -*- coding: utf-8 -*-
"""Telegram bot"""
import os
import time
import telebot
import cloudinary
import cloudinary.uploader
import cloudinary.utils
import cloudinary.api

TOKEN = os.environ['TELEGRAM_TOKEN']
BOT = telebot.TeleBot(TOKEN)
COUNT = int(0)
cloudinary.config(
    cloud_name="eu-sep",
    api_key="511481921314569",
    api_secret="ERbXpHjdMlU91qcBEslQCY5ReyE"
)


def upload(photo, name):
    """Uploads user-uploaded image onto Cloudinary"""
    cloudinary.uploader.upload(
        "https://api.telegram.org/file/bot" + TOKEN + "/" + name,
        public_id=name)


PHOTO_ARRAY = [
    'https://avatars3.githubusercontent.com/u/10268386?u=c22979fe17a17df6aa32d3cf7326e8370160dd47',
    'https://avatars1.githubusercontent.com/u/4401928?s=400&v=4'
]


@BOT.message_handler(content_types=['photo'])
def user_uploads_photo(photo):
    """When user uploads an image"""
    name = BOT.get_file(photo.photo[-1].file_id).file_path
    upload(photo, name)


@BOT.message_handler(content_types=['document'])
def user_uploads_document(message):
    """When user uses the wrong upload button"""
    BOT.reply_to(
        message, "Please use the attach image button instead of attaching a document")


@BOT.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Default command"""
    BOT.reply_to(message, "Testing 12345")


@BOT.message_handler(commands=['start_test'])
def start_test():
    """Retrieve images from Cloudinary and save to photo array"""


@BOT.message_handler(func=lambda message: True)
def echo_all(message):
    """Method returns images in PHOTO_ARRAY as Options"""
    for url in PHOTO_ARRAY:
        BOT.send_message(
            message.chat.id, "[Options](" + url + ")", parse_mode="Markdown")


BOT.polling()
