#_*_coding:utf-8_*_
__author__ = 'Linhaifeng'
from core.main import Students

class register:
    """
    学生注册
    """

class score:
    """
    学生查看个人成绩
    """

def main():
    pass

def login():
    ret=Students.login()
    if ret:
            if ret['status']:
                print(ret['data'].center(60,'-'))
                main()
            else:
                print(ret['error'].center(60,'-'))