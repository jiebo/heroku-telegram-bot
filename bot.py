# -*- coding: utf-8 -*-
"""Telegram bot"""
import os
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
CHAT_TO_USER_DICTIONARY = {}


def upload(url):
    """Uploads user-uploaded image onto Cloudinary"""
    cloudinary.uploader.upload(
        url,
        use_filename=True,
        unique_filename=True)


def downloadimagefile(url):
    """Download image from URL and save into temp file"""
    f = open(CONST_TEMP_IMAGE_FILE_NAME, 'wb')
    f.write(urllib.request.urlopen(url).read())
    f.close()


@BOT.message_handler(content_types=['photo'])
def user_uploads_photo(photo):
    """When user uploads an image"""
    filename = BOT.get_file(photo.photo[-1].file_id).file_path
    url = "https://api.telegram.org/file/bot" + TOKEN + "/" + filename
    username = photo.from_user.username

    if username not in USER_IMAGE_DICTIONARY:
        USER_IMAGE_DICTIONARY[photo.from_user.username] = [0]
    USER_IMAGE_DICTIONARY[photo.from_user.username].append(url)
    BOT.reply_to(photo.chat, 'Image uploaded.')


@BOT.message_handler(content_types=['document'])
def user_uploads_document(message):
    """When user uses the wrong upload button"""
    BOT.reply_to(
        message, "Please use the attach image button instead of attaching a document")


@BOT.message_handler(commands=['create_test'])
def create_test(message):
    """Initialize the hashmap where username is key"""
    USER_IMAGE_DICTIONARY[message.chat.username] = [0]
    BOT.reply_to(message, "Proceed to upload your images, " +
                 "and call /start_test in your target chat group after you are done")


@BOT.message_handler(commands=['end_test'])
def end_test(message):
    """Remove key value pair from dictionary so that other users can use bot in chat and display results"""
    chat_id = message.chat.id
    username = message.chat.username
    username_of_test_owner = CHAT_TO_USER_DICTIONARY[chat_id]
    result_reply = 'Result is a draw.'

    if username_of_test_owner == username:
        del username_of_test_owner
        result = USER_IMAGE_DICTIONARY[username][0]
        if result > 0:
            result_reply = "Option1 has more votes."
        elif result < 0:
            result_reply = "Option2 has more votes."

    BOT.send_message(message, "Test has ended. " + result_reply)


@BOT.message_handler(commands=['start_test'])
def start_test(message):
    """Retrieve images from hashmap and display as images"""
    username = message.chat.username
    chat_id = message.chat.id
    if username not in USER_IMAGE_DICTIONARY:
        BOT.send_message(chat_id, "You do not have images linked to you. Please upload your images again.")
        return

    if chat_id in CHAT_TO_USER_DICTIONARY:
        BOT.send_message(chat_id, "Test in progress. Please end previous test.")
        return

    initialiseChatToUser(message)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)

    for idx, url in enumerate(USER_IMAGE_DICTIONARY[username]):
        if idx == 0:
            continue
        downloadimagefile(url)
        photo = open(CONST_TEMP_IMAGE_FILE_NAME, 'rb')
        BOT.send_photo(chat_id, photo, '/Option' + str(idx))
        option_btn = telebot.types.KeyboardButton("/Option" + str(idx))
        markup.add(option_btn)

    BOT.send_message(chat_id, "Which is the best?", reply_markup=markup)


def initialiseChatToUser(message):
    chat_id = message.chat.id
    CHAT_TO_USER_DICTIONARY[chat_id] = []
    CHAT_TO_USER_DICTIONARY[chat_id] = message.chat.username


@BOT.message_handler(commands=['Option1', 'Option2'])
def retrieve_response(message):
    print (message)
    chat_id = message.chat.id
    username_of_test_owner = CHAT_TO_USER_DICTIONARY[chat_id]
    test = USER_IMAGE_DICTIONARY[username_of_test_owner]
    if message.text == '/Option1':
        test[0] += 1
    else:
        test[0] -= 1

    if test[0] > 0:
        print ("First image won: " + str(test[0]))
    else:
        print ("Second image won: " + str(test[0]))


BOT.polling()
