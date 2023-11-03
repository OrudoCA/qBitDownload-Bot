#!/usr/bin/python3
# -- coding: utf-8 --

import func, telebot, os, log, sys
from db import PATH
from lang import LANG as msg

TOKEN = os.environ.get('TOKEN','None')
bot = telebot.TeleBot(TOKEN)
folder_list = []
dir = None

# Start
@bot.message_handler(commands=['start'])
def welcome(message):
    id = message.from_user.id
    if func.auth_check(id):
        bot.reply_to(message,str(msg.get('type')),reply_markup=home())
    else:
        bot.reply_to(message,str(msg.get('adeny')))

# Keyboard: Homepage
def home():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    file = telebot.types.KeyboardButton(str(msg.get('file')))
    magnet = telebot.types.KeyboardButton(str(msg.get('magnet')))
    keyboard.add(file,magnet)
    return keyboard

# Login
@bot.message_handler(commands=['login'])
def login(message):
    id = message.from_user.id
    name = message.from_user.first_name
    passwd = message.text.replace('/login ', '')
    f = str(func.u_auth(name,id,passwd))
    if f == str(msg.get('sucauth')) or f == str(msg.get('alauth')):
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
        global folder_list
        folder_list = []
        lst = []
        for folder in folders.keys():
            globals()[f'var_{i}'] = telebot.types.KeyboardButton(f'{folder}')
            lst.append(f'var_{i}')
            folder_list.append(folder)
            i += 1
        for var in lst:
            keyboard.add(globals()[var])
        return keyboard

# Folder add
@bot.message_handler(commands=['add'])
def add(message):
    id = message.from_user.id
    name = message.from_user.first_name
    txt = message.text.split(' ', 2)
    if len(txt) == 3:
        key = txt[1]
        path = txt[2]
        f = str(func.add_dir(name,id,key,path))
    else:
        f = str(msg.get('aerr'))
    bot.reply_to(message,f,reply_markup=home())

# Folder del
@bot.message_handler(commands=['del'])
def rm(message):
    id = message.from_user.id
    name = message.from_user.first_name
    folder = message.text.replace('/del ', '')
    f = func.del_dir(name,id,folder)
    bot.reply_to(message,str(f),reply_markup=home())

# Magnet
@bot.message_handler(func=lambda message: message.text == str(msg.get('magnet')))
def magnet(message):
    id = message.from_user.id
    if func.auth_check(id):
        global type
        type = 'magnet'
        f = folder_menu()
        if f == None:
            bot.reply_to(message,str(msg.get('cff')))
        else:
            bot.reply_to(message,str(msg.get('chf')),reply_markup=f)
    else:
        bot.reply_to(message,str(msg.get('adeny')))

# File
@bot.message_handler(func=lambda message: message.text == str(msg.get('file')))
def file(message):
    id = message.from_user.id
    if func.auth_check(id):
        global type
        type = 'file'
        f = folder_menu()
        if f == None:
            bot.reply_to(message,str(msg.get('cff')))
        else:
            bot.reply_to(message,str(msg.get('chf')),reply_markup=f)
    else:
        bot.reply_to(message,str(msg.get('adeny')))

# File download
@bot.message_handler(content_types=['document'])
def download(message):
    id = message.from_user.id
    name = message.from_user.first_name
    if func.auth_check(id):
        global type, dir, folder_list
        if dir != None and type == 'file':
            if message.document.file_name.lower().endswith('.torrent'):
                file_info = bot.get_file(message.document.file_id)
                file_path = file_info.file_path
                file = bot.download_file(file_path)
                file_name = os.path.join(PATH, message.document.file_name)
                with open(file_name, 'wb') as dl:
                    dl.write(file)
                f = str(func.file(name,id,file_name,dir))
                dir, type, folder_list = None,None,[]
                bot.reply_to(message,f)
            else:
                bot.reply_to(message,str(msg.get('ntorr')))
        bot.reply_to(message,str(msg.get('type')),reply_markup=home())
    else:
        bot.reply_to(message,str(msg.get('adeny')))

# Dir choose
def dirchoose(message):
    global dir
    dir = message.text
    if type == 'magnet':
        bot.reply_to(message,str(msg.get('sendm')))
    if type == 'file':
        bot.reply_to(message,str(msg.get('sendf')))

# Unknown message
@bot.message_handler(func=lambda message: True)
def unknown(message):
    global type, dir, folder_list
    id = message.from_user.id
    name = message.from_user.first_name
    if func.auth_check(id):
        txt = message.text
        if txt in folder_list:
            dirchoose(message)
            return None
        if dir != None and type == 'magnet':
            f = str(func.magnet(name,id,txt,dir))
            dir, type, folder_list = None,None,[]
            bot.reply_to(message,f)
        bot.reply_to(message,str(msg.get('type')),reply_markup=home())
    else:
        bot.reply_to(message,str(msg.get('adeny')))

def run():
    if os.path.exists(PATH) == False:
        os.mkdir(PATH)
    log.start()
    try:
        func.qbt()
    except:
        log.errqbt()
        sys.exit(1)
    try:
        bot.polling()
    except:
        log.errtelebot()
        sys.exit(1)

if __name__ == "__main__":
    run()
