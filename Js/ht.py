import telebot
from telebot import types

bt = telebot.TeleBot('5596781204:AAEvKsQeCHiIjpbvFxn945DdLKu4Qp5jNgQ', parse_mode = None)



@bt.message_handler(content_types=   'text')
def start_messange(message):
    if message.text == 'Привет':
        bt.send_message(message.chat.id, 'Хай, ты пришел ко мне? Ну тогда пиши button')
    elif message.text == '/help':
        bt.send_message(message.chat.id, 'Пиши Привет')
    else:
        bt.send_message(message.chat.id, 'Извени, я тебя не понимаю, приши /help')



@bt.message_handler(commands=['button'])
def button_messande(messange):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton('Тетрис')
    item2 = types.KeyboardButton('Змейка')
    markup.add(item1)
    markup.add(item2)
    bt.send_message(messange.chat.id, 'Выбери что тебе по душе', reply_markup = markup  )
bt.polling()

@bt.message_handler(content_types ='text')
def start_message(message):
    bt.send_message(message.chat.id, "Извени, я тебя не понимаю, пиши /start")