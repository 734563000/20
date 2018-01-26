#_*_coding:utf-8_*_
# -*- coding:utf-8-*-
# Author:Eio

from core.main import Admin
from core.main import School
from core.main import Teacher
from core.main import Course
from core.main import Classes
from core.main import Students

def class_info():
    for obj in Classes.get_all_obj_list():
        # if obj.teacher == name
        print('\033[33;1m老师[%s] 级别[%s] 创建时间[%s]\033[0m'.center(60,'-') \
              %(obj.name,obj.level,obj.create_time))


def student_info():
    for obj in Students.get_all_obj_list():
        print(obj.name)


def set_student_score():
    """
    设置学生分数
    """


def main():
    pass

def login():
    ret=Teacher.login()
    if ret:
            if ret['status']:
                print(ret['data'].center(60,'-'))
                main()
            else:
                print(ret['error'].center(60,'-'))


if __name__ == '__main__':
    main()