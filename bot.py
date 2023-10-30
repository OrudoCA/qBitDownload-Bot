#!/usr/bin/python3
# -- coding: utf-8 --

import func, telebot, os
from db import PATH

TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(TOKEN)
folder_list = []
dir = None

# Start
@bot.message_handler(commands=['start'])
def welcome(message):
    id = message.from_user.id
    if func.auth_check(id):
        bot.reply_to(message,'Выберите тип загрузки:',reply_markup=home())
    else:
        bot.reply_to(message,'Этот бот запривачен, гнида, блять')

# Keyboard: Homepage
def home():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    file = telebot.types.KeyboardButton('Файл')
    magnet = telebot.types.KeyboardButton('Magnet-ссылка')
    keyboard.add(file,magnet)
    return keyboard

# Login
@bot.message_handler(commands=['login'])
def login(message):
    id = message.from_user.id
    passwd = message.text.replace('/login ', '')
    f = func.u_auth(id,passwd)
    if f == 'Вы успешно авторизировались' or f == 'Вы уже авторизированны':
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
    txt = message.text.split(' ', 2)
    if len(txt) == 3:
        key = txt[1]
        path = txt[2]
        f = func.add_dir(id,key,path)
    else:
        f = 'Неверные аргументы'
    bot.reply_to(message,f,reply_markup=home())

# Folder del
@bot.message_handler(commands=['del'])
def rm(message):
    id = message.from_user.id
    folder = message.text.replace('/del ', '')
    f = func.del_dir(id,folder)
    bot.reply_to(message,str(f),reply_markup=home())

# Magnet
@bot.message_handler(func=lambda message: message.text == 'Magnet-ссылка')
def magnet(message):
    id = message.from_user.id
    if func.auth_check(id):
        global type
        type = 'magnet'
        f = folder_menu()
        if f == None:
            bot.reply_to(message,'Папок не обнаруженно, воспользуйтесь коммандой /add')
        else:
            bot.reply_to(message,'Выберите папку:',reply_markup=f)
    else:
        bot.reply_to(message,'Этот бот запривачен, гнида, блять')

# File
@bot.message_handler(func=lambda message: message.text == 'Файл')
def file(message):
    id = message.from_user.id
    if func.auth_check(id):
        global type
        type = 'file'
        f = folder_menu()
        if f == None:
            bot.reply_to(message,'Папок не обнаруженно, воспользуйтесь коммандой /add')
        else:
            bot.reply_to(message,'Выберите папку:',reply_markup=f)
    else:
        bot.reply_to(message,'Этот бот запривачен, гнида, блять')

# File download
@bot.message_handler(content_types=['document'])
def download(message):
    id = message.from_user.id
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
                f = func.file(id,file_name,dir)
                dir, type, folder_list = None,None,[]
                bot.reply_to(message,f)
            else:
                bot.reply_to(message,'Неверное расширение файла')
        bot.reply_to(message,'Выберите тип загрузки:',reply_markup=home())
    else:
        bot.reply_to(message,'Этот бот запривачен, гнида, блять')

# Dir choose
def dirchoose(message):
    global dir
    dir = message.text
    if type == 'magnet':
        bot.reply_to(message,'Отправте Magnet-ссылку')
    if type == 'file':
        bot.reply_to(message,'Отправте .torrent файл')

# Unknown message
@bot.message_handler(func=lambda message: True)
def unknown(message):
    global type, dir, folder_list
    id = message.from_user.id
    if func.auth_check(id):
        txt = message.text
        if txt in folder_list:
            dirchoose(message)
            return None
        if dir != None and type == 'magnet':
            f = func.magnet(id,txt,dir)
            dir, type, folder_list = None,None,[]
            bot.reply_to(message,f)
        bot.reply_to(message,'Выберите тип загрузки:',reply_markup=home())
    else:
        bot.reply_to(message,'Этот бот запривачен, гнида, блять')

bot.polling()
