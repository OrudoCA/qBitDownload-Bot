#!/usr/bin/python3
# -- coding: utf-8 --

import os

def main():
    lang = {}
    env = os.environ['LANG']
    if env == None:
        lang = russian
    return lang

# RU
russian = {}

# ENG
english = {}
