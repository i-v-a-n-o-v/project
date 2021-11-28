import telebot
import json
import config
from db_func import get_books

bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(content_types=['text'])
def mesa(message):
    mess = str(get_books(message.text)).strip('[]')
    bot.send_message(message.chat.id, mess)

#RUN
bot.polling(none_stop=True)
