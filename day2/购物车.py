#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio
#购物列表
msg_dic=[
    ('apple\t',10),
    ('tesla\t',100000),
    ('mac\t\t',3000),
    ('lenovo\t',30000),
    ('chicken',100),
]
#标志位
flag=True
#错误次数标志位
error_count=0
max_error_count=2
#计算菜单长度(方便修改菜单后还要修改代码)
list_num=[]
for i in range(len(msg_dic)):
    list_num.append(i)
#购物车列表
shop_car=[]

while flag:
    #检查登录错误次数
    if error_count > max_error_count:
        print('Excessive number of errors ! exit ')
        break
    username=input('username:').strip()
    password=input('password:').strip()
    with open('db.txt','r') as f:
        db = f.read().split('|')
    if username != db[0] or password != db[1] :
        print('username or password error!')
        error_count+=1
        continue
    print('Login successfully !')
    #输入工资判断
    while flag:
        salary = input('Your salary is:').strip()
        if not salary.isdigit():
            print('please keyin number')
            continue
        else:
            balance = int(salary)
            break
    # 打印菜单
    while flag:
        print('menu star'.center(24, '*'))
        print('No.', 'Name  ', '\t\t', 'Price')
        for i in msg_dic:
            print(msg_dic.index(i), ' ', i[0], '\t', i[1])
        print('end'.center(24, '*'))
        choice = input('Input the No. of the item you want to purchase[q=quit]>>:').strip()
        if choice == 'q' or choice == 'quit':
            print('You have already bought %s,balance is %s' %(shop_car,balance))
            flag = False
            break
        if  not choice.isdigit():
            print('Please enter the correct NO.')
            continue
        choice = int(choice)
        if choice not in list_num:
            print('Please enter the correct NO.')
            continue
        while True:
            choice_num = input('Input the quantity you want to buy [q=quit]>>:').strip()
            if choice == 'q' or choice == 'quit':
                print('You have already bought %s,balance is %s' % (shop_car,balance))
                flag = False
                break
            if not choice_num.isdigit():
                print('please keyin number or out of rang')
                continue
            choice_num = int(choice_num)
            #判断数量是否为0
            if choice_num < 1:
                print('Must be more than 1 !')
                continue
            order = msg_dic[choice][1] * choice_num
            break
        if order < balance:
            balance = balance - order
            shop_car.append(( msg_dic[choice][0].strip('\t'),choice_num))
            print('Purchase success! %s,Your balance is %d'%(shop_car,balance))


