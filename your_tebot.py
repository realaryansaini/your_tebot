# import telegram.ext

# Token = "5765371571:AAGZj-fW0hG-EG1qR8pCz9Nz1kgJtyY_dhQ"

# updater = telegram.ext.Updater("5765371571:AAGZj-fW0hG-EG1qR8pCz9Nz1kgJtyY_dhQ", use_context=true)
# dispatcher = updater.dispatcher
# def start(update,context):
#     update.message.reply_text("Hello thanks for creating me")

# dispatcher.add_handler(telegram.ext.CommandHandler("start",start))
# updater.start_polling()
# updater.idle()

import os

import telebot

BOT_TOKEN = "5765371571:AAHPzJE1klb1guwcUyGRlvuTaAzZFPziPJU" #os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


#Let's define a message handler that handles incoming /start and /hello commands.
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "welcome")
@bot.message_handler(regexp="hello")
@bot.message_handler(regexp="hey")
def send_welcome(message):
    bot.reply_to(message, "Hello")
@bot.message_handler(regexp="jarvis")
def send_welcome(message):
    bot.reply_to(message, "sir sir")    
#Let’s add another handler that echoes all incoming text messages back to the sender.
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


#ou now have a simple bot that responds to the /start and /hello commands with a static message and echoes all the other sent messages. Add the following to the end of your file to launch the bot:
bot.infinity_polling()