#!/usr/bin/envpython
# -*- coding:utf-8-*-
# Author:Eio

import time
from core import auth
from core import logger
from core.auth import login_required

#日志不懂
#transaction logger
trans_logger = logger.logger('transaction')
#access logger
access_logger = logger.logger('access')





@login_required
def account_info(acc_data):
    # print(acc_data)
    print('用户名:%s\n余额:%s\n信用额度:%s'%(acc_data['account_id'],\
                                    acc_data['account_data'][acc_data['account_id']]['balance'], \
                                    acc_data['account_data'][acc_data['account_id']]['credit']))

#还款
@login_required
def repay(acc_data):
    print('还款')

#取款
@login_required
def withdraw():
    print('取款')

#转账
@login_required
def transfer():
    print('转账')

#账单
@login_required
def pay_check():
    print('账单')

def logout(acc_data):
    print('再见 ! %s'%(acc_data['account_id']))
    exit()

def logout1(acc_data):
    interactive(user_data)

#注册
def reg():
    pass



#定义一个初始的用户登录状态变量
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}
#定义一个购物车
shop_car = []


def interactive(acc_data):
    '''
    interact with user
    :return:
    '''
    menu = u'''
    ----------------------
    1.  商城
    2.  ATM
    3.  注册用户
    4.  退出
    '''
    menu_dic = {
        '1': interactive_shop,
        '2': interactive_atm,
        '3': reg,
        '4': logout,
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
            print("选项不存在")


def interactive_atm(acc_data):
    '''
    interact with user
    :return:
    '''
    menu = u'''
    ------- Oldboy Bank ---------
    1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  退出
    '''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout1,
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
            print("选项不存在")


def interactive_shop(acc_data):
    salary = acc_data['account_data'][acc_data['account_id']]['balance']
    welcome_msg = 'welcome to oldboy shoping mall'
    print(welcome_msg.center(50, '-'))  # .center（距离，字符）

    product_list = [
        ('Iphone', 5888),
        ('Mac Air', 8000),
        ('XiaoMi', 19.9),
        ('coffee', 30),
    ]

    # 标志位
    exit_flag = 0
    while exit_flag is not True:
        print('商城物品列表:'.center(50, '-'))
        for item in enumerate(product_list):  # 实现更加优美的索引
            index = item[0]  # 获得商品序号
            p_name = item[1][0]  # 获得商品名称
            p_price = item[1][1]  # 获得商品价格
            print(index, p_name, p_price)

        user_choice = input('选择你要购买的物品?q 退出,c 查看已购物品:')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list):  # 输入的商品序号要在范围之内
                p_item = product_list[user_choice]  # 选择的商品
                if p_item[1] <= salary:  # 买得起
                    shop_car.append(p_item)  # 放入购物车
                    salary -= p_item[1]  # 减钱
                    print('已购买的物品:'.center(40, '-'))
                    for item in shop_car:
                        print(item)
                    print('你的余额是 [%s]' % salary)
                    time.sleep(2)
                else:  # 买不起
                    print('你的余额是 [%s],无法购买所选产品!' % salary)
                    time.sleep(2)
            else:
                print('输入错误!')
                time.sleep(2)
        elif user_choice == 'q' or user_choice == 'quit':
            print('已购买的物品:'.center(40, '-'))
            for item in shop_car:
                print(item)
            print('结束'.center(40, '-'))
            print('你的余额是 [%s]' % salary)
            time.sleep(2)
            exit_flag = True
        elif user_choice == 'c' or user_choice == 'check':
            print('已购买的物品:'.center(40, '-'))
            for item in shop_car:
                print(item)
            print('你的余额是 %d' % salary)
            print('结束'.center(40, '-'))
            time.sleep(2)
        else:
            print('输入错误!')











def run():
    '''
    这是开始就启动的一个主程序,判断用户登录状态
    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)