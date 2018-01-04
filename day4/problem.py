# ll=range(1,9)
# # lo=ll.__iter__()
# # print(next(lo))
# # print(next(lo))
# #
# #
# for i  in range(1,9):
#     print(i)

# def foo():
#     print('1')
#     yield 1
#     print('2')
#     yield 2
#     print('3')
#     yield 3
#
# obj=foo()
# print(next(obj))
# print(next(obj))


# import time
# def tail(filepath):
#     with open(filepath,'rb') as f:
#         f.seek(0,2)
#         while True:
#             line=f.readline()
#             if line:
#                 yield line
#             else:
#                 time.sleep(0.05)
#
# def grep(lines,pattern):
#     for line in lines:
#         line=line.decode('utf-8')
#         if pattern in line:
#             yield line
#
#
# lines=grep(tail('access.log'),'404')
# for line in lines:
#     print(line)
#


# def eater(name):
#     print('%s readt to eat'%name)
#     while True:
#         food=yield
#         print('%s start to eat %s'%(name,food))
#
# e=eater('alex')
#
# e.send(None)
# e.send('一桶狗粮')
# e.send('一桶骨头')

import os

def init(func):
    def inner(*args,**kwargs):
        res=func(*args,**kwargs)
        next(res)
        return res
    return inner


# def search(target):
#     while True:
#         filepath = yield
#         g = os.walk(filepath)
#         for parth,_,files in g:
#             for file in files:
#                 abs_path=r'%s\%s'%(parth,file)
#                 target.send(abs_path)

@init
def search(target):  # r'D:\video\python20期\day4\a'
    while True:
        filepath = yield
        g = os.walk(filepath)
        for pardir, _, files in g:
            for file in files:
                abs_path = r'%s\%s' % (pardir, file)
                #把abs_path传给下一个阶段
                print(abs_path)



# @init
# def opener(target):
#     nua=0
#     while True:
#         print(nua)
#         yield 1
#         print('opener func====')




g=search('opener')
next(g)
g.send(r'D:\python\20\day4')
















