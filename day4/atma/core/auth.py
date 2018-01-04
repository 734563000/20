#!/usr/bin/envpython
# -*- coding:utf-8-*-
# Author:Eio

import json

#验证登录装饰器
def login_required(func):
    #验证用户是否登录
    def wrapper(*args,**kwargs):
        #print('--wrapper--->',args,kwargs)
        if args[0].get('is_authenticated'):
            return func(*args,**kwargs)
        else:
            exit("用户未认证!")
    return wrapper




#通过读取文件信息.来判断用户是否有效,如果有效返回数据
def acc_auth(account,password):
    with open('../db/db.json', 'r') as f:
        account_data = json.load(f)
        if account and account in account_data:
            if password == account_data[account]['password']:
                print('登录成功')
                return account_data
            else:
                print('密码错误')
        else:
            print("账号不存在")



#认证程序
def acc_login(user_data,log_obj):
    '''
    :return:
    '''
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3 :
        account = input("用户名:").strip()
        password = input("密码:").strip()
        auth = acc_auth(account, password)
        if auth: #如果有返回数据.则写入登录状态
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth
        retry_count +=1#失败则在错误次数+1
    else:
        #登录次数过多记录在文件中
        log_obj.error("account [%s] too many login attempts" % account)
        exit()
