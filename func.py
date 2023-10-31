#!/usr/bin/python3
# -- coding: utf-8 --

import db, os 
from db import *

def qbt():
    url = os.environ['QURL']
    username = os.environ['QUSER']
    password = os.environ['QPASS']
    commands = [
            f"qbt settings set url {url}",
            f"qbt settings set username {username}",
            f"echo {password} | qbt settings set password --no-warn"
            ]
    for command in commands:
        os.system(f"bash -c '{command}'")

def u_auth(id,passwd):
    list = []
    if db.check('obj',AUTH_FILE):
        list = db.read(AUTH_FILE)
    if id in list:
        return 'Вы уже авторизированны'
    else:
        if passwd == os.environ['PASS']: 
            list.append(id)
            db.write(list,AUTH_FILE)
            return 'Вы успешно авторизировались'
        else:
            return 'Неверный пароль'

def auth_check(id):
    if db.check('obj',AUTH_FILE):
        list = db.read(AUTH_FILE)
    else:
        list = []
    if id in list:
        return True

def add_dir(id,dir,path):
    if auth_check(id):
        if os.path.exists(path) == False:
            return f"Директории '{path}' не сушествует на сервере"
        if db.check('obj',DIR_FILE):
            dict = db.read(DIR_FILE)
        else:
            dict = {}
        dict.setdefault(dir,path)
        db.write(dict,DIR_FILE)
        return f"Папка {dir} успешно добавлена"
    else:
        return 'Этот бот запривачен, гнида, блять'

def del_dir(id,dir):
    if auth_check(id):
        if db.check('obj',DIR_FILE):
            dict = db.read(DIR_FILE)
        else:
            dict = {}
        if dir in dict:
            del dict[dir]
            db.write(dict,DIR_FILE)
            return f"Папка {dir} успешно удалена"
        else:
            return f"Папки {dir} не существует"
    else:
        return 'Этот бот запривачен, гнида, блять'

def magnet(id,link,dir):
    if auth_check(id):
        dict = db.read(DIR_FILE)
        path = dict[dir]
        command = f'''qbt torrent add url "{link} -f {path}"'''
        os.system(f"bash -c '{command}'")
        return 'Torrent добавлен в очередь'
    else:
        return 'Этот бот запривачен, гнида, блять'

def file(id,file,dir):
    if auth_check(id):
        dict = db.read(DIR_FILE)
        path = dict[dir]
        command = f'''qbt torrent add file "{file}" -f {path}'''
        os.system(f"bash -c '{command}'")
        os.remove(file)
        return 'Torrent добавлен в очередь'
    else:
        return 'Этот бот запривачен, гнида, блять'

def dirlist():
    dirs = {}
    if db.check('obj',DIR_FILE):
        dirs = db.read(DIR_FILE)
    return dirs
