#!/usr/bin/python3
# -- coding: utf-8 --

import pickle, os

PATH = "/etc/bot/"
AUTH_FILE= "auth.pkl"
DIR_FILE = "dir.pkl"

def check(type,FILE):
    if type == 'dir':
        if os.path.exists(PATH) == False:
            os.mkdir(PATH)
        return True
    elif type == 'obj':
        if os.path.exists(f'{PATH}{FILE}'):
            return True
        else:
            return False

def write(obj,FILE):
    if check('dir',None):
        with open(f'{PATH}{FILE}',"wb") as file:
            pickle.dump(obj,file)

def read(FILE):
    with open(f'{PATH}{FILE}',"rb") as file:
        obj = pickle.load(file)
    return obj
