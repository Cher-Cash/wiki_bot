import telebot
from config import config
from wiki import page_by_name

bot = telebot.TeleBot(config['token'])
@bot.message_handler(commands=['start'])
def start(message):
    greeting = 'Привет, я умею находить определения на интересующие тебя термины. Напиши, о чем бы ты хотел узнать.'
    bot.send_message(message.chat.id, greeting)


@bot.message_handler(content_types=['text'])
def start(message):
    incoming_mes = message.text
    answer = page_by_name(incoming_mes)
    bot.send_message(message.chat.id, answer)





bot.infinity_polling()