#!/usr/bin/envpython
# -*- coding:utf-8-*-
# Author:Eio

import os
import sys
import logging

#程序在系统中的目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#已经将DB文件写死位置
# DATABASE = {
#     'engine': 'file_storage', #support mysql,postgresql in the future
#     'name':'accounts',
#     'path': "%s/db" % BASE_DIR
# }

#日志模块(不懂,未动)
LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}


#ATM费率文件
TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},

}