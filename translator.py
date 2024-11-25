from telebot import TeleBot
from deep_translator import GoogleTranslator
from config import *

translator = GoogleTranslator(source='en', target='uz')
bot = TeleBot(token=TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f'Добро пожаловать {message.from_user.first_name} в переводчик!')
    give_me_word(message)



def give_me_word(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Отправьте слово, которое нужно перевести!')
    bot.register_next_step_handler(msg, translate_word)

def translate_word(message):
    chat_id = message.chat.id
    translated_text = translator.translate(message.text)
    bot.send_message(chat_id, translated_text,)
    give_me_word(message)

bot.polling(none_stop=True)