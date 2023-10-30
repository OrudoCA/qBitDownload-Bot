#!/usr/bin/python3
# -- coding: utf-8 --

import db, os, subprocess
from db import *

def u_auth(id,passwd):
    list = []
    if db.check('obj',AUTH_FILE):
        list = db.read(AUTH_FILE)
    if id in list:
        return 'You already logged in'
    else:
        if passwd == os.environ['PASS']: 
            list.append(id)
            db.write(list,AUTH_FILE)
            return 'Success'
        else:
            return 'Wrong password'

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
            return 'Folder not exist on host'
        if db.check('obj',DIR_FILE):
            dict = db.read(DIR_FILE)
        else:
            dict = {}
        dict.setdefault(dir,path)
        db.write(dict,DIR_FILE)
        return 'Success'
    else:
        return 'Log in first'

def del_dir(id,dir):
    if auth_check(id):
        if db.check('obj',DIR_FILE):
            dict = db.read(DIR_FILE)
        else:
            dict = {}
        if dir in dict:
            del dict[dir]
            db.write(dict,DIR_FILE)
            return 'Success'
        else:
            return 'Dir not exists'
    else:
        return 'Log in first'

def magnet(id,link,dir):
    if auth_check(id):
        dict = db.read(DIR_FILE)
        path = dict[dir]
        command = f'''qbt torrent add url "{link} -f {path}"'''
        os.system(f"bash -c '{command}'")
        return 'Success'
    else:
        return 'Log in first'

def file(id,file,dir):
    if auth_check(id):
        subprocess.run(f"qbt torrent add file {PATH}{file} -f {dir}", check=True, shell=True)
        os.remove(f'{PATH}{file}')
        return 'Success'

def dirlist():
    dirs = {}
    if db.check('obj',DIR_FILE):
        dirs = db.read(DIR_FILE)
    return dirs
