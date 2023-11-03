#!/usr/bin/python3
# -- coding: utf-8 --

import os

langs = ['ENG','RU']

# Russian
RU = {
        'alauth': 'Вы уже авторизированны',
        'sucauth': 'Вы успешно авторизировались',
        'wrauth': 'Неверный пароль',
        'pne': "Директории '{}' не сушествует на сервере",
        'fsa': "Папка '{}' успешно добавлена",
        'frm': "Папка '{}' успешно удалена", 
        'fne': "Папки '{}' не существует",
        'add': 'Torrent добавлен в очередь',
        'type': 'Выберите тип загрузки:',
        'magnet': 'Magnet-ссылка',
        'file': 'Файл',
        'aerr': 'Неверные аргументы',
        'cff': 'Папок не обнаруженно, воспользуйтесь коммандой /add',
        'chf': 'Выберите папку:',
        'ntorr': 'Неверное расширение файла',
        'sendm': 'Отправте Magnet-ссылку',
        'sendf': 'Отправте .torrent файл',
        'adeny': 'Этот бот запривачен, гнида, блять',
        # Logs
        'l_create': "Log Файл '{}' создан",
        'l_start': 'Запуск бота...',
        'l_auth': "Пользователь '{} ({})' успешно авторизировался",
        'l_add': "Пользователь '{} ({})' добавил папку '{}' по пути '{}'",
        'l_rm': "Пользователь '{} ({})' удалил папку '{}'",
        'l_file': "Пользователь '{} ({})' добавил в очередь файл '{}'",
        'l_magnet': "Пользователь '{} ({})' добавил в очередь ссылку '{}'",
        'l_errqbt': "Ошибка подключения к qBitTorrent",
        'l_errtele': "Ошибка подключения к Telegram API, проверьте ваш токен",
        }

# English
ENG = {
        'alauth': 'You are already authorized',
        'sucauth': 'You have successfully logged in',
        'wrauth': 'Wrong password',
        'pne': "The '{}' directory does not exist on the server",
        'fsa': "The '{}' folder has been successfully added",
        'frm': "The '{}' folder has been successfully deleted", 
        'fne': "The '{}' folder does not exist",
        'add': 'Torrent has been added to the queue',
        'type': 'Select the download type:',
        'magnet': 'Magnet',
        'file': 'File',
        'aerr': 'Wrong arguments',
        'cff': 'No folders found, use the /add command',
        'chf': 'Select folder:',
        'ntorr': 'Incorrect file extension',
        'sendm': 'Send Magnet link',
        'sendf': 'Send .torrent file',
        'adeny': "You do not have access, first authorize '/login <password>'",
        # Logs
        'l_create': "Log File '{}' created",
        'l_start': 'Start bot polling...',
        'l_auth': "User '{} ({})' successfully authorized",
        'l_add': "User '{} ({})' added a folder '{}' with the path '{}'",
        'l_rm': "User '{} ({})' deleted '{}' folder",
        'l_file': "User '{} ({})' added file '{}' to the queue",
        'l_magnet': "User '{} ({})' added the link '{}' to the queue",
        'l_errqbt': "Error connecting to qBitTorrent",
        'l_errtele': "Error connecting to Telegram API, check your token"
        }

for i in langs:
    if i == os.environ.get('LANG','ENG'):
        LANG = globals()[i]
