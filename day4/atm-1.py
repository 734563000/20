#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import json

msg_dic=[
    ('apple\t',10),
    ('tesla\t',100000),
    ('mac\t\t',3000),
    ('lenovo\t',30000),
    ('chicken',100),
]
creditline=15000
shop_car=[]
account_file='config'
user_info={}
error_count=0
max_error_count=2
Charge=0.05
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
        return db[username]
    else:
        return None

def shoppingmall(acc_data):
    global shop_car
    balance = db_read(acc_data['name'])['Creditline'] - db_read(acc_data['name'])['consumption']
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
        choice_num = input('Input the quantity you want to buy >>:').strip()
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
            print("I'm sorry. You don't accept cash for the time being")
            continue
        if choice == '2' or choice == 'Credit Card':
            balance = int(acc_data['Creditline'] - acc_data['consumption'])
            # print(order,balance)
            if order < balance:
                balance_new = acc_data['Creditline'] - (acc_data['consumption'] + order)
                shop_car.append((msg_dic[choice_item][0].strip('\t'), choice_num))
                acc_data['consumption'] = acc_data['consumption'] + order
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
    \033[32;1m1.  Shopping mall
    2.  ATM
    3.  Log out
    \033[0m'''
    menu_dic = {
        '1': shoppingmall,
        '2': bank_menu,
        '3': logout
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

def bank_menu(acc_data):
    menu = u'''
    --------- Bank ---------
    \033[32;1m 1. Account information
     2. Repay
     3. Withdrawals
     4. Transfer
     5. Billing
     6. Exit
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
            # print('accdata',acc_data)
            #acc_data['is_authenticated'] = False
            menu_dic[user_option](acc_data)
        else:
            print("\033[31;1mOption does not exist!\033[0m")

def account_info(acc_data):
    # print(acc_data)

    print('name:\t%s\ncash:\t%s\nCredit line:\t%s\nCredits:\t%s'%(acc_data['name'],\
                                    acc_data['cash'], \
                                    acc_data['Creditline'],
                                    acc_data['Creditline'] - acc_data['consumption']))

def repay(acc_data):
    cash = int(db_read(acc_data['name'])['cash'])
    salary = int(db_read(acc_data['name'])['consumption'])
    while True:
        money = input('Please enter the amount of payment you want to pay:').strip()
        if not money.isdigit():
            print('please keyin number')
            continue
        break
    money = int(money)
    if cash >= money:
        cash_new = cash - money
        salary_new = salary - money
        acc_data['cash'] = cash_new
        acc_data['consumption'] = salary_new
        db_write(acc_data['name'], acc_data)
        print('Repayment success ! ')
    else:
        print('Cash not enough !')

def withdraw(acc_data):
    cash = int(db_read(acc_data['name'])['cash'])
    salary = int(db_read(acc_data['name'])['consumption'])
    while True:
        money = input('Please enter the amount you want to withdraw cash:').strip()
        if not money.isdigit():
            print('please keyin number')
            continue
        break
    money = int(money)
    if salary >= money:
        sc= money * Charge
        cash_new = cash + money - sc
        salary_new = salary + money
        acc_data['cash'] = cash_new
        acc_data['consumption'] = salary_new
        db_write(acc_data['name'], acc_data)
        print('Successful withdrawal ! Your service charge is %s' %sc)
    else:
        print('Money not enough')

def transfer(acc_data):
    print("I'm sorry. It's not finished yet.")

def pay_check(acc_data):
    print("I'm sorry. It's not finished yet.")

def logout(acc_data):
    print('bye bye ! %s' % (acc_data['name']))
    exit()

def manager_menu(acc_data):
    menu = u'''
    --------- Menu ---------
    \033[32;1m1.  Add an account
    2.  Change User quota
    3.  Lock account
    4.  Main menu
    5.  Log out
    \033[0m'''
    menu_dic = {
        '1': addacc,
        '2': changequota,
        '3': lockacc,
        '4': main_menu,
        '5': logout
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

def addacc(acc_data):
    name = input('Please enter your registration name:').strip()
    passwd = input('Please enter your registration name:').strip()
    with open(account_file) as f:
        data = json.load(f)
    data[name]={'name': name, 'password': passwd, 'Creditline': creditline, 'consumption': 0, 'cash': 0, 'status': "0"}
    with open(account_file, 'w') as f:
        json.dump(data,f)
    print('registration success !')

def changequota(acc_data):
    while True:
        cname = input('Please enter the user name you want to change:')
        with open(account_file) as f:
            acc_data = json.load(f)
        if cname not in acc_data:
            print('username error !')
            continue
        break
    while True:
        quota_new = input('Please enter the credit you want to adjust:').strip()
        if not quota_new.isdigit():
            print('please keyin number')
            continue
        break
    acc_data = db_read(cname)
    acc_data['Creditline'] = quota_new
    db_write(acc_data['name'], acc_data)
    print('Change successfully ! please login again')
    exit()

def lockacc(acc_data):
    while True:
        cname = input('Please enter the user name you want to change:')
        with open(account_file) as f:
            acc_data = json.load(f)
        if cname not in acc_data:
            print('username error !')
            continue
        break
    while True:
        status_new = input('Please enter the state you want to change(0:normal 1:locked):').strip()
        if not status_new.isdigit():
            print('please keyin number')
            continue
        # status_new = int(status_new)
        if status_new not in ('1','0') :
            print('out of rangs !')
            continue
        break
    acc_data = db_read(cname)
    acc_data['status'] = status_new
    db_write(acc_data['name'], acc_data)
    print('Change successfully ! please login again')
    exit()

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
    if res['status'] == "0":
        print('Login successfully !')
        main_menu(res)
    if res['status'] == "1":
        print('Your account has been locked !')
        exit()
    if res['status'] == "3":
        print('Welcome administrator !')
        manager_menu(res)

if __name__ == '__main__':
    main()