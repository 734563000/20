#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

from conf import settings

import json

current_status={'user':None,'login_status':None}


def auth(func):
    def inner(*args,**kwargs):
        if settings.acc_data:
            res = func(*args, **kwargs)
            return  res
        while True:
            if settings.error_count > settings.max_error_count:
                print('Excessive number of errors ! exit ')
                exit()
            username = input('username:').strip()
            password = input('password:').strip()
            with open(settings.account_file) as f:
                db = json.load(f)
            if username not in db:
                print('username error!')
                settings.error_count += 1
                continue
            if password == db[username]['password']:
                settings.acc_data = db[username]
                res = func(*args, **kwargs)
                return res
            else:
                continue
    return inner