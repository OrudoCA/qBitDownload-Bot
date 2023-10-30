#!/usr/bin/python3
# -- coding: utf-8 --

import func, telebot, os

TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(TOKEN)

# Start
@bot.message_handler(commands=['start'])
def welcome(message):
    id = message.from_user.id
    if func.auth_check(id):
        bot.reply_to(message,'Choose download type:',reply_markup=home())
    else:
        bot.reply_to(message,'Log in to use bot /login <passwd>')

# Keyboard: Homepage
def home():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    file = telebot.types.KeyboardButton('File')
    magnet = telebot.types.KeyboardButton('MagnetLink')
    keyboard.add(file)
    keyboard.add(magnet)
    return keyboard

# Login
@bot.message_handler(commands=['login'])
def login(message):
    id = message.from_user.id
    passwd = message.text.replace('/login ', '')
    f = func.u_auth(id,passwd)
    if f == 'Success' or f == 'You already logged in':
        bot.reply_to(message,f,reply_markup=home())
    else:
        bot.reply_to(message,f)

# Folders
def folder_menu():
    folders = func.dirlist()
    if len(folders) == 0:
        return None
    else:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        i = 0  
        lst = []
        for folder in folders.keys():
            globals()[f'var_{i}'] = telebot.types.KeyboardButton(f'{folder}')
            lst.append(f'var_{i}')
            i += 1
        for var in lst:
            keyboard.add(globals()[var])
        return keyboard

# Folder add
@bot.message_handler(commands=['add'])
def add(message):
    id = message.from_user.id
    txt = message.text.split(' ', 2)
    if len(txt) == 3:
        key = txt[1]
        path = txt[2]
        f = func.add_dir(id,key,path)
    else:
        f = 'Invalid args'
    bot.reply_to(message,f,reply_markup=home())

# Folder del
@bot.message_handler(commands=['del'])
def rm(message):
    id = message.from_user.id
    folder = message.text.replace('/del ', '')
    f = func.del_dir(id,folder)
    bot.reply_to(message,str(f),reply_markup=home())


# Magnet
@bot.message_handler(func=lambda message: message.text == 'MagnetLink')
def magnet(message):
    id = message.from_user.id
    if func.auth_check(id):
        f = folder_menu()
        if f == None:
            bot.reply_to(message,'No folders, use /add <folder_name> <path>')
        else:
            bot.reply_to(message,'Choose dir:',reply_markup=f)
    else:
        bot.reply_to(message,'Log in to use bot /login <passwd>')

# Unknown message
@bot.message_handler(func=lambda message: True)
def unknown(message):
    id = message.from_user.id
    if func.auth_check(id):
        bot.reply_to(message,'Choose download type:',reply_markup=home())
    else:
        bot.reply_to(message,'Log in to use bot /login <passwd>')

bot.polling()