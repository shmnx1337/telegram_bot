import telebot
from settings import  TG_API_TOKEN 
from bot_logic import gen_pass
from bot_logic import gen_moneta
bot = telebot.TeleBot(TG_API_TOKEN)


# виды обработчиков:

# шаблон обработчика
# @bot_message_handler(<критерий обработки>)
# def func(message):
# ...

# 1) обработчик команды
@bot.message_handler(commands=['start', 'help']) # /start, /help
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет! Я твой первый бот в тг :)')

# 2) обработчик типа сообщения
@bot.message_handler(content_types=['sticker']) # 'audio', 'photo', 'voice', 'sticker', 'document', 'video', 'text', 'location'
def handle_sticker(message):
    bot.reply_to(message, 'крутой стикер!')

# 3) обработчик с собственным критерием
@bot.message_handler(func=lambda message: message.text.lower().count('а') > 3)
def handle_a(message):
    bot.reply_to(message, 'ААААААААААААААААААААА')

@bot.message_handler(commands=['password'])
def send_password(message):
    password = gen_pass(10)
    bot.send_message(message.chat.id, f'Ваш пароль: {password}')
@bot.message_handler(commands=['moneta'])
def handle_moneta(message):
    result = gen_moneta()  
    bot.send_message(message.chat.id, f"Монета подброшена: {result}")
bot.infinity_polling()
