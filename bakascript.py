import telebot

token = "556161272:AAFoP3abycmprZXz3NpjfwRuZ6PVwelkLpw"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "start!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text)

bot.polling()
