#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio
# import os,sys
# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
from lib import auth
from lib import db
from conf import settings
from core import atm
from core import shop
import json



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

@auth.auth
def run():
    res = settings.acc_data
    if res['status'] == "0":
        print('Login successfully !')
        main_menu(res)
    if res['status'] == "1":
        print('Your account has been locked !')
        exit()
    if res['status'] == "3":
        print('Welcome administrator !')
        manager_menu(res)

@auth.auth
def main_menu(acc_data):
    menu = u'''
    --------- Menu ---------
    \033[32;1m1.  Shopping mall
    2.  ATM
    3.  Log out
    \033[0m'''
    menu_dic = {
        '1': shop.shoppingmall,
        '2': atm.bank_menu,
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

@auth.auth
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
        '1': atm.addacc,
        '2': atm.changequota,
        '3': atm.lockacc,
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
    with open(settings.account_file) as f:
        data = json.load(f)
    data[name]={'name': name, 'password': passwd, 'Creditline': settings.creditline, 'consumption': 0, 'cash': 0, 'status': "0"}
    with open(settings.account_file, 'w') as f:
        json.dump(data,f)
    print('registration success !')

def changequota(acc_data):
    while True:
        cname = input('Please enter the user name you want to change:')
        with open(settings.account_file) as f:
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
    acc_data = db.db_read(cname)
    acc_data['Creditline'] = quota_new
    db.db_write(acc_data['name'], acc_data)
    print('Change successfully ! please login again')
    exit()

def lockacc(acc_data):
    while True:
        cname = input('Please enter the user name you want to change:')
        with open(settings.account_file) as f:
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
    acc_data = db.db_read(cname)
    acc_data['status'] = status_new
    db.db_write(acc_data['name'], acc_data)
    print('Change successfully ! please login again')
    exit()

def logout(acc_data):
    print('bye bye ! %s' % (acc_data['name']))
    exit()