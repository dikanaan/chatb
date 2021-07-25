import requests, json, time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


intro = ('AI CHAT BOT HALUSINASI\n\n'
'\nDibuat karena kegabutan melanda dunia, source code hubungi @dikanaan'
'\nAPI : http://fdciabdul.tech'

'\n\nJika ada masalah dalam BOT hubungi @dikanaan'
)




def head(message):
    id_chat = message['chat']['id']
    command = message['text']
    dari = message['from']['id']
    nama = message['from']['first_name']
    #uer = message['from']['username']
    #print(nama+'\n'+uer+'\n'+command)
    print(nama)
    pesan = (message['text'])
    resp = requests.get("https://fdciabdul.tech/api/ayla?pesan="+pesan)
    jawab = resp.json()['jawab']
    print(jawab)
    api_bot.sendMessage(id_chat, jawab)
    if command == '/start' or command == '/help':
        content_type, chat_type, id_chat = telepot.glance(message)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Donasi', url='https://saweria.co/dikanaan')],])
        api_bot.sendMessage (id_chat, str(intro),reply_markup=keyboard)
        

      

api_bot = telepot.Bot('1939896494:AAH1F6u35byYR9wMNClXCJ3y_0Sank28N2o')
MessageLoop(api_bot, head).run_as_thread()
print('Running..')

while 1:
    time.sleep(10)
