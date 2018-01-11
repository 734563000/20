#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
account_file=os.path.join(BASE_DIR,'db','db')
# account_file='db'
LOG_PATH=os.path.join(BASE_DIR,'log','log.log')


msg_dic=[
    ('apple\t',10),
    ('tesla\t',100000),
    ('mac\t\t',3000),
    ('lenovo\t',30000),
    ('chicken',100),
]

creditline=15000

shop_car=[]

user_info={}

error_count=0

max_error_count=2

Charge=0.05

list_num=[]

acc_data={}

for i in range(len(msg_dic)):
    list_num.append(i)