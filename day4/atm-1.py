#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import json
import os
msg_dic=[
    ('apple\t',10),
    ('tesla\t',100000),
    ('mac\t\t',3000),
    ('lenovo\t',30000),
    ('chicken',100),
]

shop_car=[]
account_file='db'
user_info={}
error_count=0
max_error_count=2
list_num=[]
for i in range(len(msg_dic)):
    list_num.append(i)

def login(username,password):
    global error_count
    with open(account_file) as f:
        db = json.load(f)
    if username not in db:
        print('username error!')
        error_count+=1
        return None
    if password == db[username]['password']:
        print('Login successfully !')
        return db[username]
    else:
        return None

def shoppingmall(acc_data):
    global shop_car
    balance = db_read(acc_data['name'])['salary']
    print(balance)
    while True:
        print('menu star'.center(24, '*'))
        print('No.', 'Name  ', '\t\t', 'Price')
        for i in msg_dic:
            print(msg_dic.index(i), ' ', i[0], '\t', i[1])
        print('end'.center(24, '*'))
        choice = input('Input the No. of the item you want to purchase[q=quit,i=info]>>:').strip()
        if choice == 'q' or choice == 'quit':
            print('You have already bought %s,balance is %s' % (shop_car, balance))
            flag = False
            return
        if choice == 'i' or choice == 'info':
            print('You have already bought %s,balance is %s' % (shop_car, balance))
            continue
        if not choice.isdigit():
            print('Please enter the correct NO.')
            continue
        choice = int(choice)
        if choice not in list_num:
            print('Please enter the correct NO.')
            continue
        choice_num = input('Input the quantity you want to buy [q=quit]>>:').strip()
        if not choice_num.isdigit():
            print('please keyin number or out of rang')
            continue
        choice_num = int(choice_num)
        # 判断数量是否为0
        if choice_num < 1:
            print('Must be more than 1 !')
            continue
        order = msg_dic[choice][1] * choice_num
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
            print("You don't have cash!")
            continue
        if choice == '2' or choice == 'Credit Card':
            balance = int(db_read(acc_data['name'])['salary'])
            print(order,balance)
            if order < balance:
                balance_new = balance - order
                shop_car.append((msg_dic[choice_item][0].strip('\t'), choice_num))
                acc_data['salary'] = balance_new
                db_write(acc_data['name'],acc_data)
                print('Purchase success! %s,Your balance is %d' % (shop_car, balance_new))
                return True
            else:
                print('Your balance is not enough')
                return False
        print("\033[31;1mOption does not exist!\033[0m")



def db_read(username):
    with open(account_file) as f:
        acc_data = json.load(f)
        return  acc_data[username]

def db_write(name,acc_data):
    with open(account_file, 'r') as f:
        account_data = json.load(f)
        account_data[name]=acc_data
    with open(account_file, 'w') as f:
        json.dump(account_data,f)
        return True

def main_menu(acc_data):
    menu = u'''
    --------- Menu ---------
    \033[32;1m1.  购物商城
    2.  ATM
    \033[0m'''
    menu_dic = {
        '1': shoppingmall,
        '2': bank_menu,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            # print('accdata:',acc_data)
            #acc_data['is_authenticated'] = False
            menu_dic[user_option](acc_data)
        else:
            print("\033[31;1mOption does not exist!\033[0m")

def bank_menu():
    menu = u'''
    --------- Bank ---------
    \033[32;1m1.  账户信息
    2.  还款(功能已实现)
    3.  取款(功能已实现)
    4.  转账
    5.  账单
    6.  退出
    \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            print('accdata',acc_data)
            #acc_data['is_authenticated'] = False
            menu_dic[user_option](acc_data)
        else:
            print("\033[31;1mOption does not exist!\033[0m")

def main():
    while True:
        if error_count > max_error_count:
            print('Excessive number of errors ! exit ')
            exit()
        username=input('username:').strip()
        password=input('password:').strip()
        res = login(username,password)
        if res != None:
            break
    main_menu(res)



if __name__ == '__main__':
    main()