#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio


class School:
    name='Oldboy'
    def __init__(self,addr,course):
        self.addr=addr
        self.course=course
    def create_cls(self):
        """创建班级, 关联课程讲师"""
        pass


class Sudents:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
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

class Teacher:
    def __init__(self, name, sex, age,courses,addr):
        self.name=name
        self.sex=sex
        self.age=age
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