# coding: utf-8
import re
import time
import telepot
from telepot.loop import MessageLoop
from compress import arithm_decode, arithm_encode, bwt_decode, bwt_encode
import prettymsg

type_compress = None


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(msg)

    if content_type == 'text':
        text = msg['text'].strip()
        message_is_arifm = re.match(r'арифм .+$', text.lower())
        message_is_bwt = re.match(r'bwt .+$', text.lower())
        message_is_command = re.match(r'/[a-z_]+$', text.lower())

        if message_is_command:
            if text == '/start':
                firstname = msg['from'].get('first_name')
                bot.sendMessage(chat_id, u'Добро пожаловать, ' + firstname + u'!')

        elif message_is_arifm:
            word = text.split()[1]
            n = len(word)
            code, code_str, sorted_freqs, sorted_ranges, new_ranges = arithm_encode(word)
            calc = arithm_decode(n, code, sorted_ranges)
            answer = prettymsg.arifm(code, code_str, sorted_freqs, sorted_ranges, new_ranges, calc)

        elif message_is_bwt:
            word = text.split()[1]
            top_list, code, index = bwt_encode(word)
            solve, s = bwt_decode(code, index)
            answer = prettymsg.bwt(top_list, code, index, solve, s)

        bot.sendMessage(chat_id, answer)


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
