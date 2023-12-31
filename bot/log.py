#!/usr/bin/python3
# -- coding: utf-8 --

import os, uuid
from datetime import datetime
from lang import LANG as msg
from db import PATH

def dt():
    date = datetime.now().date()
    time = datetime.now().time()
    str = f'{date} | {time.strftime("%H:%M:%S")}'
    return str

DEFAULT = ['{} LOG: ','{} ERROR: ']
ID = str(uuid.uuid1())[0:7]
FILE = f'{ID}.txt'

def file(log):
    if os.path.exists(f'{PATH}logs') == False:
        os.mkdir(f'{PATH}logs')
    with open(f'{PATH}logs/{FILE}','a') as logfile:
        logfile.write(f'{log}\n')
        logfile.close()

def start():
    log1 = DEFAULT[0].format(dt()) + str(msg.get('l_create').format(FILE))
    log2 = DEFAULT[0].format(dt()) + str(msg.get('l_start'))
    file(log2)
    print(f'{log1}\n{log2}')

def auth(name,id):
    log = DEFAULT[0].format(dt()) + str(msg.get('l_auth').format(name,id))
    file(log)
    print(log)

def add(name,id,folder,path):
    log = DEFAULT[0].format(dt()) + str(msg.get('l_add').format(name,id,folder,path))
    file(log)
    print(log)

def rm(name,id,folder):
    log = DEFAULT[0].format(dt()) + str(msg.get('l_rm').format(name,id,folder))
    file(log)
    print(log)

def addfile(name,id,filename):
    log = DEFAULT[0].format(dt()) + str(msg.get('l_file').format(name,id,filename[9:]))
    file(log)
    print(log)

def addmagnet(name,id,link):
    log = DEFAULT[0].format(dt()) + str(msg.get('l_magnet').format(name,id,link))
    file(log)
    print(log)

def errqbt():
    log = DEFAULT[1].format(dt()) + str(msg.get('l_errqbt'))
    file(log)
    print(log)

def errtelebot():
    log = DEFAULT[1].format(dt()) + str(msg.get('l_errtele'))
    file(log)
    print(log)
