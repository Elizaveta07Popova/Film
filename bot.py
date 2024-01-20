import telebot
import random
API_TOKEN="6525210612:AAHGGa8VMg3Ii52tFujEJYQOrHdNZ2w6Ac8"
bot=telebot.TeleBot(API_TOKEN)
from telebot import types

@bot.message_handler(commands=['start'])
def knopka(message):
    markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton("Что посмотреть?"))
    bot.send_message(message.chat.id,"Привет! Давай выберем фильм на вечер.",reply_markup=markup)

@bot.message_handler(content_types=["text"])
def any_msg(message):
    if message.text == "Что посмотреть?":
        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton(text="посмеяться", callback_data="1")
        but2 = types.InlineKeyboardButton(text="испугаться", callback_data="2")
        but3 = types.InlineKeyboardButton(text="поплакать", callback_data="3")
        but4 = types.InlineKeyboardButton(text="задуматься", callback_data="4")
        but5 = types.InlineKeyboardButton(text="Про спорт", callback_data="5")
        keyboard.add(but1, but2)
        keyboard.add(but3, but4)
        keyboard.add(but5)
        bot.send_message(message.chat.id, "Фильм, чтобы...", reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    if call.data == "1":
        with open("1.txt", "r", encoding="utf-8") as file:
            c = file.read().split("\n")
        cont = random.choice(c)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=cont)
    elif call.data == "2":
        with open("2.txt", "r", encoding="utf-8") as file:
            c = file.read().split("\n")
        cont = random.choice(c)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=cont)
    elif call.data == "3":
        with open("3.txt", "r", encoding="utf-8") as file:
            c = file.read().split("\n")
        cont = random.choice(c)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=cont)
    elif call.data == "4":
        with open("4.txt", "r", encoding="utf-8") as file:
            c = file.read().split("\n")
        cont = random.choice(c)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=cont)
    elif call.data == "5":
        with open("5.txt", "r", encoding="utf-8") as file:
            c = file.read().split("\n")
        cont = random.choice(c)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=cont)


bot.infinity_polling()