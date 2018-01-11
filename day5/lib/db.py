#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio
from conf import settings
import json

def db_read(username):
    with open(settings.account_file) as f:
        acc_data = json.load(f)
        return  acc_data[username]

def db_write(name,acc_data):
    with open(settings.account_file, 'r') as f:
        account_data = json.load(f)
        account_data[name]=acc_data
    with open(settings.account_file, 'w') as f:
        json.dump(account_data,f)
        return True