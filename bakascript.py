import telebot
import os
import random as rand
from flask import Flask, request
import consoleweather.weather as cw
import crypt as c

token = "556161272:AAFoP3abycmprZXz3NpjfwRuZ6PVwelkLpw"

bot = telebot.TeleBot(token)

server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "start!")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, """
    /start - start
    /roll - random
    /weather - weather
    /crypt - crypt
    /uncrypt - uncrypt
    /me - me
    """)


@bot.message_handler(commands=['roll'])
def send_roll(message):
    roll = rand.randint(0,100)
    bot.send_message(message.chat.id, roll)

@bot.message_handler(commands=['weather'])
def send_weather(message):
    bot.send_message(message.chat.id,"`" + cw.get_weather() + "`", parse_mode='Markdown')

@bot.message_handler(commands=['crypt'])
def send_crypt(message):
    usrtxt = message.text.replace("/crypt","")
    print(message)
    if(usrtxt):
        bot.reply_to(message, c.crypt(usrtxt))
    else:
        bot.send_message(message.chat.id, "я не могу зашифровать пустую строку")

@bot.message_handler(commands=['uncrypt'])
def send_uncrypt(message):
    usrtxt = message.text.replace("/uncrypt","")
    if(usrtxt):
        bot.reply_to(message, c.uncrypt(usrtxt))
    else:
        bot.send_message(message.chat.id, "я не могу расшифровать пустую строку")

@bot.message_handler(commands=['me'])
def send_me(message):
    #bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id,
    "_" + message.from_user.first_name + " " + message.text.replace("/me","") + "_",
    parse_mode='Markdown')
    if message.chat.type == "group":
        bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(commands=['anon'])
def send_anon(message):
    bot.forward_message(-377257708, message.chat.id - 1, message.message_id)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text)

#bot.polling()

@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://bakatestapp.herokuapp.com/' + token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
