#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import pickle
from conf import settings
import os



class Funtion:
    def datasave(self,objname):
        pickle.dump(self,open(os.path.join(settings.db_dir,objname),'wb'))
    def dataload(self,objname):
        ret=[]
        for i in settings.db_dir:
            obj=pickle.load(open(os.path.join(settings.db_dir,objname),'rb'))
            ret.append(obj)
        return ret

class School:
    def __init__(self,name,addr,course):
        self.name=name
        self.addr=addr
        self.course=course
    def create_cls(self):
        """创建班级, 关联课程讲师"""
        pass

class People:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

class Sudents(People):
    def __init__(self,name,sex,age):
        super().__init__(name,sex,age)


    def register(self):
        """注册"""
        pass

    def pay_money(self):
        """交学费"""
        pass

    def select_class(self):
        """选择班级"""
        pass

class Course:
    def __init__(self,name,cycle,price):
        self.name = name  # 课程名
        self.cycle=cycle  # 周期
        self.price=price  # 价格

class Teacher(People):
    def __init__(self,name,sex,age,courses,addr):
        super().__init__(name,sex,age)
        self.courses=courses
        self.addr=addr

    def manage_class(self):
        """管理班级"""
        pass

    def select_class(self, cls):
        """选择班级"""
        pass

    def view_students(self, cls):
        """查看班级学员列表"""
        pass

    def change_fraction(self, name, fraction):
        """修改学员成绩"""
        pass