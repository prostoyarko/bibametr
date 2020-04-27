import telebot
import random

bot = telebot.TeleBot('1129979286:AAG-s9qWwo4UfYuQ-1LTRcSZRO6J72Om8dY')
f=random.randrange(5,25)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привіт!', 'Поміряти пісюн', 'Знайти щура')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI8hF6EkNHYVsfRFto2lycu36MVxCenAAIVAANlpDIU9QmVaqMnu3AYBA', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привіт!':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI8gl6Ej_J3duh-ib0_XQkdG8w0ZM8nAAIuAANlpDIUo11rOhNxjqQYBA')
    elif message.text.lower() == 'поміряти пісюн':
        a=random.randint(5,25)
        bot.send_message(message.chat.id,  'Твій пісюн '+  str(a)  + ' см')
        if a <= 13:
            bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAJVnl6hrEz3j1r4S8XQqrpQhtY-mbiBAAIyAANlpDIUCz1nVg7rfZsYBA")
            bot.send_message(message.chat.id, "Ахаха, лошара")
        elif 22 >= a > 13 :
            bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAJAVF6OwzVb_9mu0DDEUxmCJdNVVJsXAALtAAO0gEokRDvBA-Hu8YsYBA")
        elif a > 22:
            bot.send_message(message.chat.id, "Вітаю! Щастя тобі і благополуччя")
            bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAJVoF6hrpt21URJrvpjybGH4zSf21BsAAI5AANlpDIUxxVcRobIa6kYBA")
    elif message.text.lower() == 'знайти щура':
        bot.send_sticker(message.chat.id,  'CAACAgIAAxkBAAI8hl6Ek4cH-OPF4h06FnC0_oBlus3WAAIwAANlpDIU2CIRaOdzqOkYBA')






bot.polling()