#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio
import os
import logging
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
account_file=os.path.join(BASE_DIR,'config','config')
# account_file='db'
LOG_PATH=os.path.join(BASE_DIR,'log','log.log')
JYLOG_PATH=os.path.join(BASE_DIR,'log','transaction.log')



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



#1、Logger：产生日志
jy=logging.getLogger('交易记录')
lg=logging.getLogger('日志记录')
# logger2=logging.getLogger('错吴日志')


#2、Filter：几乎不用

#3、Handler：接收Logger传过来的日志，进行日志格式化，可以打印到终端，也可以打印到文件
sh=logging.StreamHandler() #打印到终端
fh1=logging.FileHandler(LOG_PATH,encoding='utf-8')
fh2=logging.FileHandler(JYLOG_PATH,encoding='utf-8')


#4、Formatter：日志格式
formatter1=logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)
formatter2=logging.Formatter(
    fmt='%(asctime)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)
formatter3=logging.Formatter(
    fmt='%(asctime)s : %(module)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)

#5、为handler绑定日志格式
sh.setFormatter(formatter1)
fh1.setFormatter(formatter2)
fh2.setFormatter(formatter2)

#6、为logger绑定handler
jy.addHandler(sh)
jy.addHandler(fh2)
lg.addHandler(sh)
lg.addHandler(fh1)


#7、设置日志级别:logger对象的日志级别应该＜＝handler的日志界别
# logger1.setLevel(50)
jy.setLevel(10)
lg.setLevel(10)
sh.setLevel(10)
fh1.setLevel(10)
fh2.setLevel(10)

