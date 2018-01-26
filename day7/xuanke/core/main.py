#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import pickle,time,os
from conf import settings
from core import id




class BaseModel:
    def save(self):
        # 获取目录路径,类名为目录.uuid为文件名
        file_path=os.path.join(self.db_path,str(self.nid))
        # 存放数据
        pickle.dump(self,open(file_path,'wb'))

    @classmethod
    def get_all_obj_list(cls):
        ret=[]
        for filename in os.listdir(cls.db_path):
            file_path = os.path.join(cls.db_path,filename)
            ret.append(pickle.load(open(file_path,'rb')))
        return ret

class School(BaseModel):
    db_path = settings.SCHOOL_DB_DIR
    def __init__(self,name,addr):
        self.nid=id.SchoolNid(self.db_path)
        self.name=name
        self.addr=addr
        self.create_time=time.strftime('%Y-%m-%d %X')

    def __str__(self):
        return self.name

    def create_cls(self):
        """创建班级, 关联课程讲师"""
        pass

class Course(BaseModel):
    db_path = settings.COURSE_DB_DIR
    def __init__(self, name, price, period, school_nid):
        self.nid = id.CourseNid(self.db_path)
        self.name = name   #课程名
        self.price = price  #价格
        self.period = period#周期
        self.school_nid = school_nid #学校信息

class Coure2teacher(BaseModel):
    db_path = settings.COURSE_TO_TEACHER_DB_DIR
    def __init__(self,course_nid,school_nid):
        self.nid=id.Course2TeacherNid(self.db_path)
        self.course_nid=course_nid
        self.school_nid=school_nid

    def get_course_to_teacher_list(self):
        ret=self.get_all_obj_list()
        if ret:
            return [ret.course_nid.get_obj_by_uuid(),ret.classes_nid.get_obj_by_uuid()]
        return [None,None]

class Classes(BaseModel):
    db_path=settings.CLASSES_DB_DIR
    def __init__(self,name,tuition,school_nid,course_to_teacher_list):
        self.nid=id.ClassesNid(self.db_path)
        self.name=name
        self.tuition=tuition
        self.school_nid=school_nid
        self.course_to_teacher_list=course_to_teacher_list

class Students(BaseModel):
    db_path=settings.STUDENT_DB_DIR
    def __init__(self,name,age,qq,classes_nid):
        self.nid = id.StudentNid(self.db_path)
        self.name = name
        self.age = age
        self.qq = qq
        self.classes_nid = classes_nid
        self.score=Score(self.nid)

    @staticmethod
    def login():#登录功能
        try:
            name=input('user: ').strip()
            for obj in Students.get_all_obj_list():
                if obj.name == name:
                    status = True
                    error=''
                    data='登录成功'
                    break
            else:
                raise Exception('学生用户名不存在!')
        except Exception as e:
            status=False
            error=str(e)
            data=''
        return {'status':status,'error':error,'data':data}

class Teacher(BaseModel):
    db_path=settings.TEACHER_DB_DIR
    def __init__(self,name,level,schoolnid):
        self.nid = id.TeacherNid(self.db_path)
        self.name = name
        self.level = level
        self.schoolnid = schoolnid
        self.create_time=time.strftime('%Y-%m-%d %X')

    @staticmethod
    def login():#登录功能
        try:
            name=input('user: ').strip()
            for obj in Teacher.get_all_obj_list():
                if obj.name == name:
                    status = True
                    error=''
                    data='登录成功'
                    break
            else:
                raise Exception('教师用户名错误')
        except Exception as e:
            status=False
            error=str(e)
            data=''
        return {'status':status,'error':error,'data':data}

class Admin(BaseModel):
    db_path = settings.ADMIN_DB_DIR
    def __init__(self,username,passwd):
        self.nid=id.AdminNid(self.db_path)
        self.username = username
        self.passwd = passwd

    @staticmethod
    def login():#登录功能
        try:
            name=input('user: ').strip()
            pas=input('passwd: ').strip()
            for obj in Admin.get_all_obj_list():
                if obj.username == name and obj.passwd == pas:
                    status = True
                    error=''
                    data='登录成功'
                    break
            else:
                raise Exception('用户名或密码错误')
        except Exception as e:
            status=False
            error=str(e)
            data=''
        return {'status':status,'error':error,'data':data}

class Score:
    def __init__(self,nid):
        self.nid=nid
        self.score_dict={}

    def set(self,course_to_teacher_nid,number):
        self.score_dict[course_to_teacher_nid]=number

    def get(self,course_to_teacher_nid):
        return self.score_dict.get(course_to_teacher_nid)