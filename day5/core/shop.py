#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

from conf import settings
from lib import db

shop_car=[]

def shoppingmall(acc_data):
    global shop_car
    balance = db.db_read(acc_data['name'])['Creditline'] - db.db_read(acc_data['name'])['consumption']
    print(balance)
    while True:
        print('menu star'.center(24, '*'))
        print('No.', 'Name  ', '\t\t', 'Price')
        for i in settings.msg_dic:
            print(settings.msg_dic.index(i), ' ', i[0], '\t', i[1])
        print('end'.center(24, '*'))
        choice = input('Input the No. of the item you want to purchase[q=quit,i=info]>>:').strip()
        if choice == 'q' or choice == 'quit':
            print('You have already bought %s,balance is %s' % (shop_car, balance))
            return
        if choice == 'i' or choice == 'info':
            print('You have already bought %s,balance is %s' % (shop_car, balance))
            continue
        if not choice.isdigit():
            print('Please enter the correct NO.')
            continue
        choice = int(choice)
        if choice not in settings.list_num:
            print('Please enter the correct NO.')
            continue
        choice_num = input('Input the quantity you want to buy >>:').strip()
        if not choice_num.isdigit():
            print('please keyin number or out of rang')
            continue
        choice_num = int(choice_num)
        # 判断数量是否为0
        if choice_num < 1:
            print('Must be more than 1 !')
            continue
        order = settings.msg_dic[choice][1] * choice_num
        break
    Checkout(acc_data,choice,choice_num,order)


def Checkout(acc_data,choice_item,choice_num,order):
    while True:
        menu = u'''
        --------- Menu ---------
        \033[32;1m1.  Cash
        2.  Credit Card
        \033[0m'''
        print(menu)
        choice = input('Please choose the way of payment:').strip()
        if choice == '1' or choice == 'Cash':
            print("I'm sorry. You don't accept cash for the time being")
            continue
        if choice == '2' or choice == 'Credit Card':
            balance = int(acc_data['Creditline'] - acc_data['consumption'])
            if order < balance:
                balance_new = acc_data['Creditline'] - (acc_data['consumption'] + order)
                shop_car.append((settings.msg_dic[choice_item][0].strip('\t'), choice_num))
                acc_data['consumption'] = acc_data['consumption'] + order
                db.db_write(acc_data['name'],acc_data)
                print('Purchase success! %s,Your balance is %d' % (shop_car, balance_new))
                return True
            else:
                print('Your balance is not enough')
                return False
        print("\033[31;1mOption does not exist!\033[0m")