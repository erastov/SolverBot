# coding: utf-8
import re
import time
import telepot
from telepot.loop import MessageLoop
from compress import encode


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(msg)

    if content_type == 'text':
        text = msg['text'].strip().lower()
        message_is_command = re.match(r'/[a-z_]+$', text)

        if message_is_command:
            if text == '/start':
                firstname = msg['from'].get('first_name')
                bot.sendMessage(chat_id, u'Добро пожаловать, ' + firstname + u'!')


if __name__ == "__main__":
    TOKEN = '464271886:AAFNntR3dtxjBoO1SrdM9RGWI3SCl14Taxs'

    bot = telepot.Bot(TOKEN)
    answerer = telepot.helper.Answerer(bot)
    MessageLoop(bot, {'chat': handle,
                      }).run_as_thread()

    print('Listening ...')

    # Keep the program running.
    while 1:
        time.sleep(10)
