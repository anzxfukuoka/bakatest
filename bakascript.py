import telebot
import random as rand

token = "556161272:AAFoP3abycmprZXz3NpjfwRuZ6PVwelkLpw"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "start!")

@bot.message_handler(commands=['roll'])
def send_welcome(message):
    roll = rand.randint(0,100)
    bot.send_message(message.chat.id, roll)

@bot.message_handler(commands=['me'])
def send_welcome(message):
    bot.send_message(message.chat.id,
    "_" + message.from_user.first_name + " " + message.text.replace("/me","") + "_",
    parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text)

bot.polling()
