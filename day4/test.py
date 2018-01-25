# # # import json
# # # account_file='db'
# # # account_data={'egon':{'password':'123','salary':'15000'}}
# # # # with open(account_file, 'w') as f:
# # # #     acc_data = json.dump(account_data,f)
# # #
# # #
# # #
# # # with open(account_file) as f:
# # #     acc_data = json.load(f)
# # # print(acc_data['egon']['password'])
# #
# #
# #
# # import time
# # current_status={'user':None,'login_status':False}
# #
# # def timmer(func):
# #     def inner(*args,**kwargs):
# #         start_time=time.time()
# #         res=func(*args,**kwargs)
# #         stop_time=time.time()
# #         print('run time is :[%s]' %(stop_time-start_time))
# #         return res
# #     return inner
# #
# # def auth(egine='file'):
# # # egine='file'
# #     def wrapper(func):
# #         def inner(*args,**kwargs):
# #             if current_status['user'] and current_status['login_status']:
# #                 res = func(*args, **kwargs)
# #             return res
# #         return inner
# #     return wrapper
# #
# # def index(egine):
# #     if egine == 'file':
# #         u='egon'
# #         p='123'
# #     elif egine == 'mysql':
# #         u = 'egon'
# #         p = '123'
# #     elif egine == 'ldap':
# #         u = 'egon'
# #         p = '123'
# #     else:
# #         pass
# #
# # name = input('username>>:').strip()
# # pwd = input('password>>:').strip()
# # if name == u and pwd == p:
# #     print('login successfull')
# #     current_status['user'] = name
# #     current_status['login_status'] = True
# #     res = func(*args, **kwargs)
# #
# #
# #
# # @timmer
# # @auth(egine='ldap') #@wrapper #index=wrapper(timmer_inner)
# # # @timmer #timmer_inner=timmer(index)
# # def index():
# # time.sleep(3)
# # print('welcome to index page')
# # return 123
# #
# #
# # index() #inner()
#
# # print(bool(123))
#
#
# import logging
# #1、Logger：产生日志
# logger1=logging.getLogger('访问日志')
# # logger2=logging.getLogger('错吴日志')
#
#
# #2、Filter：几乎不用
#
# #3、Handler：接收Logger传过来的日志，进行日志格式化，可以打印到终端，也可以打印到文件
# sh=logging.StreamHandler() #打印到终端
# fh1=logging.FileHandler('s1.log',encoding='utf-8')
# fh2=logging.FileHandler('s2.log',encoding='utf-8')
#
# #4、Formatter：日志格式
# formatter1=logging.Formatter(
#     fmt='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
# )
# formatter2=logging.Formatter(
#     fmt='%(asctime)s : %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
# )
# formatter3=logging.Formatter(
#     fmt='%(asctime)s : %(module)s : %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
# )
#
# #5、为handler绑定日志格式
# sh.setFormatter(formatter1)
# fh1.setFormatter(formatter2)
# fh2.setFormatter(formatter3)
#
# #6、为logger绑定handler
# logger1.addHandler(sh)
# logger1.addHandler(fh1)
# logger1.addHandler(fh2)
#
# #7、设置日志级别:logger对象的日志级别应该＜＝handler的日志界别
# # logger1.setLevel(50)
# logger1.setLevel(10) #
# sh.setLevel(10)
# fh1.setLevel(10)
# fh2.setLevel(10)
#
# #8、测试
# logger1.debug('测试着玩')
# logger1.info('运行还算正常')
# logger1.warning('可能要有bug了')
# logger1.error('不好了，真tm出bug了')
# logger1.critical('完犊子，推倒重写')

# import re
#
# print(re.findall('\w','egon 123 + _ - *'))
# print(re.findall('\W','egon 123 + _ - *'))
# print(re.findall('\s','ego\tn 12\n3 + _ - *'))
# print(re.findall('\S','ego\tn 12\n3 + _ - *'))
# print(re.findall('\d','ego\tn 12\n3 + _ - *'))
# print(re.findall('\D','ego\tn 12\n3 + _ - *'))
# print(re.findall('\n','ego\tn 12\n3 + _ - *'))
# print(re.findall('\t','ego\tn 12\n3 + _ - *'))
# print(re.findall('e','ego\tn 12\n3 +hello _ - *'))
# print(re.findall('^e','ego\tn 12\n3 +hello _ - *'))
# print(re.findall('o$','ego\tn 12\n3 +hello'))


import pickle


class Schools(object):
    def __init__(self, address, account):
        self.address = address  # 学校地址
        self.account = account  # 学校账户

    @staticmethod
    def create_sub(*args, **kwargs):
        """创建课程, 课程名,周期,价格"""
        return Subject(*args, **kwargs)

    @staticmethod
    def create_cls(**kwargs):
        """创建班级, 关联课程讲师"""
        return Classes(**kwargs)

    @staticmethod
    def create_tea(**kwargs):
        """创建讲师"""
        return Teachers(**kwargs)


class Subject(object):
    def __init__(self, name, period, price):
        self.name = name      # 课程名
        self.period = period  # 课程周期
        self.price = price    # 课程价格


class Students(object):
    def __init__(self, name, fraction):
        self.name = name   # 学生名 - 标识
        self.fraction = fraction  # 学生分数

    def register(self, sch):
        """注册"""
        pass

    def pay_money(self, amount):
        """交学费"""
        pass

    def select_class(self, cls):
        """选择班级"""
        pass


class Classes(object):
    def __init__(self, num, students_list, tea, sub):
        self.tea = tea    # 关联讲师
        self.num = num    # 班级人数
        self.students_list = students_list  # 学生列表 - 里面是学生对象
        self.sub = sub    # 关联课程


class Teachers(object):
    def __init__(self, sch, name, cls):
        self.sch = sch    # 关联学校 - 对象
        self.name = name  # 老师名字
        self.cls = cls    # 关联班级 - 对象

    def manage_class(self):
        """管理班级"""
        pass

    def select_class(self, cls):
        """选择班级"""
        self.cls = cls

    def view_students(self, cls):
        """查看班级学员列表"""
        return self.cls.students_list

    def change_fraction(self, name, fraction):
        """修改学员成绩"""
        self.cls.students_list[name].fraction = fraction
