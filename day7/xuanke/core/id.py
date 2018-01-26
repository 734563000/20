#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

from lib import func
import pickle,os

class Nid:
    def __init__(self,role,db_path):
        role_list=[
            'admin','school','teacher','course','course2teacher','classes','student'
        ]
        if role not in role_list:
            raise Exception('用户角色错误,选项: %s' % ','.join(role_list))
        self.role=role
        self.uuid=func.create_uuid()
        self.db_path=db_path

    def __str__(self):
        return self.uuid

    def get_obj_by_uuid(self):
        for filename in os.listdir(self.db_path):
            if filename == self.uuid:
                return pickle.load(open(os.path.join(self.db_path,filename),'rb'))
        return None

class SchoolNid(Nid):
    def __init__(self,db_path):
        super(SchoolNid,self).__init__('school',db_path)

class TeacherNid(Nid):
    def __init__(self,db_path):
        super(TeacherNid,self).__init__('teacher',db_path)

class CourseNid(Nid):
    def __init__(self,db_path):
        super(CourseNid,self).__init__('course',db_path)

class Course2TeacherNid(Nid):
    def __init__(self,db_path):
        super(Course2TeacherNid,self).__init__('course2teacher',db_path)

class ClassesNid(Nid):
    def __init__(self,db_path):
        super(ClassesNid,self).__init__('classes',db_path)

class StudentNid(Nid):
    def __init__(self,db_path):
        super(StudentNid,self).__init__('student',db_path)

class AdminNid(Nid):
    def __init__(self,db_path):
        super(AdminNid,self).__init__('admin',db_path)
