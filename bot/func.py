#!/usr/bin/python3
# -- coding: utf-8 --

import db, os, log 
from db import *
from lang import LANG as msg

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
        return msg.get('alauth')
    else:
        if passwd == os.environ['PASS']: 
            list.append(id)
            db.write(list,AUTH_FILE)
            log.auth(id)
            return msg.get('sucauth')
        else:
            return msg.get('wrauth')

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
            return str(msg.get('pne')).format(path)
        if db.check('obj',DIR_FILE):
            dict = db.read(DIR_FILE)
        else:
            dict = {}
        dict.setdefault(dir,path)
        db.write(dict,DIR_FILE)
        log.add(id,dir,path)
        return str(msg.get('fsa')).format(dir)
    else:
        return msg.get('adeny')

def del_dir(id,dir):
    if auth_check(id):
        if db.check('obj',DIR_FILE):
            dict = db.read(DIR_FILE)
        else:
            dict = {}
        if dir in dict:
            del dict[dir]
            db.write(dict,DIR_FILE)
            log.rm(id,dir)
            return str(msg.get('frm')).format(dir)
        else:
            return str(msg.get('fne')).format(dir)
    else:
        return msg.get('adeny')

def magnet(id,link,dir):
    if auth_check(id):
        dict = db.read(DIR_FILE)
        path = dict[dir]
        command = f'''qbt torrent add url "{link}" -f "{path}"'''
        os.system(f"bash -c '{command}'")
        log.addmagnet(id,link)
        return msg.get('add')
    else:
        return msg.get('adeny')

def file(id,file,dir):
    if auth_check(id):
        dict = db.read(DIR_FILE)
        path = dict[dir]
        command = f'''qbt torrent add file "{file}" -f {path}'''
        os.system(f"bash -c '{command}'")
        os.remove(file)
        log.addfile(id,file)
        return msg.get('add')
    else:
        return msg.get('adeny')

def dirlist():
    dirs = {}
    if db.check('obj',DIR_FILE):
        dirs = db.read(DIR_FILE)
    return dirs
