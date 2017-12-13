#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio



menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


#标志位
flag=True
#存放浏览历史
history=[]

while flag:
    #打印菜单
    print('star'.center(10,'*'))
    for i in menu:
        print(i)
    print('end'.center(10,'*'))
    #等待用户输入选择
    choice=input('Please enter your choice >>:').strip()
    #是否使用退出
    if choice == 'q' or choice == 'exit':
        print('exit !')
        flag=False
    #用户是否选择返回
    if choice == 'b':
        #检查历史记录中还有没有数据
        if len(history) == 0:
            print('No more return')
        #将最后加入的菜单取出至当前菜单
        else:
            menu=history.pop(-1)
        continue
    #检查用户输入的数据在不在当前数据中
    if choice not in menu:
        print('Please enter the correct name!')
        continue
    #进入下级菜单时,将上级菜单数据存入列表
    history.append(menu)
    #进入下级菜单
    menu=menu[choice]




