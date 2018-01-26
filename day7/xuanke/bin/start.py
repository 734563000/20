#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core.services import admin_service
from core.services import teacher_service
from core.services import student_service
from core.services import initialize_service

msg = '''
0:初始化
1:管理员
2:老师
3:学生
'''

#主要启动程序
if __name__ == '__main__':
    role_main={
        '0':initialize_service.main,
        '1':admin_service.login,
        '2':teacher_service.login,
        '3':student_service.login,
    }
    while True:
        print(msg)
        choice=input('select role: ').strip()
        if choice not in role_main:continue
        role_main[choice]()