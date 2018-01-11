#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

from conf import settings
from lib import db

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
    cash = int(db.db_read(acc_data['name'])['cash'])
    salary = int(db.db_read(acc_data['name'])['consumption'])
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
        db.db_write(acc_data['name'], acc_data)
        print('Repayment success ! ')
    else:
        print('Cash not enough !')

def withdraw(acc_data):
    cash = int(db.db_read(acc_data['name'])['cash'])
    salary = int(db.db_read(acc_data['name'])['consumption'])
    while True:
        money = input('Please enter the amount you want to withdraw cash:').strip()
        if not money.isdigit():
            print('please keyin number')
            continue
        break
    money = int(money)
    if salary >= money:
        sc= money * settings.Charge
        cash_new = cash + money - sc
        salary_new = salary + money
        acc_data['cash'] = cash_new
        acc_data['consumption'] = salary_new
        db.db_write(acc_data['name'], acc_data)
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