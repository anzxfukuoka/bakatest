from PIL import Image
import telebot
import os
import io
import random as rand
from flask import Flask, request
import consoleweather.weather as cw
import crypt as c

token = "556161272:AAFoP3abycmprZXz3NpjfwRuZ6PVwelkLpw"

bot = telebot.TeleBot(token)

server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message.from_user.first_name)
    bot.send_message(message.chat.id, "привет, ̶м̶и̶р̶ " + message.from_user.first_name)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, """
        /start - start
    /help - help
    /roll - random
    /weather - погода
    /crypt - зашифровать текст
    /uncrypt - расшифровать текст
    /me [текст сообщения] - сообщение от третего лица (группа)
    /daltonic - daltonic
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
    #print(message.text)
    msg = bot.send_message(message.chat.id, "отправьте текст")
    bot.register_next_step_handler(msg, crypt_text)

def crypt_text(message):
    try:
        bot.reply_to(message, c.crypt(message.text))
    except Exception as e:
        bot.send_message(message.chat.id, "ваш текст не текст")


@bot.message_handler(commands=['uncrypt'])
def send_uncrypt(message):
    #print(message.text)
    msg = bot.send_message(message.chat.id, "отправьте зашифрованный текст")
    bot.register_next_step_handler(msg, uncrypt_text)

def uncrypt_text(message):
    try:
        bot.reply_to(message, c.uncrypt(message.text))
    except Exception as e:
        bot.send_message(message.chat.id, "ваш текст не текст")


@bot.message_handler(commands=['me'])
def send_me(message):
    #bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id,
    "_" + message.from_user.first_name + " " + message.text.replace("/me","") + "_",
    parse_mode='Markdown')
    if message.chat.type == "group":
        bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(commands=['daltonic'])
def send_daltonic(message):
    msg = bot.send_message(message.chat.id, "отправьте фото")
    bot.register_next_step_handler(msg, daltonic)
    pass

def daltonic(message):
    try:
        fileID = message.photo[-1].file_id
        file = bot.get_file(fileID)
    except:
        bot.send_message(message.chat.id, "ваше фото не фото")
        return

    downloaded_file = bot.download_file(file.file_path)

    im = Image.open(io.BytesIO(downloaded_file))
    r, g, b = im.split()
    im = Image.merge("RGB", (r, r, b))

    imgByteArr = io.BytesIO()
    im.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()

    bot.send_photo(message.chat.id, imgByteArr)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text)

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
    pass

#bot.remove_webhook()
#bot.polling()
