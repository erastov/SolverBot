# coding: utf-8
import re
import time
import telepot
from telepot.loop import MessageLoop
# from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
# from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
# import sys
#
# sys.path.insert(0, '/var/beacon/clr/scripts')
# from toolsofbot import action, add_member, get_profile_info, get_alerts, delete_member
# from toolsofbot import create_inline_buttons, create_beautiful_msg


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(msg)

    if content_type == 'text':
        text = msg['text'].strip().lower()
        message_is_command = re.match(r'/[a-z_]+$', text)

        if message_is_command:
            if text == '/start':
                firstname = msg['from'].get('first_name')
                bot.sendMessage(chat_id, u'Добро пожаловать в SAS AntiFraudBot, '
                                + firstname + u'!\nНачните работать..')



def on_callback_query(msg):
    content_type, chat_type, chat_id = telepot.glance(msg['message'])
    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')


TOKEN = '376839159:AAGRSibs1XMz9WiNNSKGsLjP9X60guevB8A'

bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)
MessageLoop(bot, {'chat': handle,
                  'callback_query': on_callback_query
                  }).run_as_thread()
print 'Listening ...'

# Keep the program running.
while 1:
    time.sleep(10)
