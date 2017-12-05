#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

dic={
    'egon1':{'password':'123','count':0},
    'egon2':{'password':'123','count':0},
    'egon3':{'password':'123','count':0},
}

flag=True       #标志位
error_count=0   #错误输入计数
count=2         #超过几次退出(加入黑名单)

while flag:
    username=input('username:').strip()
    password=input('password:').strip()
    #判断用户是否在字典中
    if username not in dic:
        #检查锁定状态
        if error_count < count:
            print('username does not exist!')
            #用户名不存在错误次数统计
            error_count += 1
            continue
        else:
            #超过登录错误次数
            print('Excessive number of errors ! exit ')
            break
    #读取黑名单
    with open('blacklist.txt', 'r') as f:
        lock_list = f.read().split(',')
        #检查用户输入的用户名是否在黑名单中
        if username in lock_list:
            print('%s is allready locked !' %username)
            break
    #检查错误次数是否达到指定次数,达到后写入黑名单
    if dic[username]['count'] > count:
        print('%s is locked !' %username)
        with open('blacklist.txt', 'a') as f:
            f.write(',%s' %username)
        break
        #检查密码是否正确
    if password == dic[username]['password']:
        #显示欢迎信息
        print('Login successfully')
        #清空登录错误次数
        dic[username]['count'] = 0
        while flag:
            cmd=input('CMD:')
            if cmd == 'q' or cmd == 'quit':
                print('exit')
                flag = False
            else:
                print('run',cmd)
    else:
        #用户存在密码错误处理
        print('password error')
        dic[username]['count']+=1
        continue

