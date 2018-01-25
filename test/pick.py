#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import pickle

dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}

# print(type(dic))  # <class 'dict'>

j = pickle.dumps(dic)
# print(type(j))  # <class 'bytes'>
#
f = open('pick', 'wb')  # 注意是w是写入str,wb是写入bytes,j是'bytes'
f.write(j)  # -------------------等价于pickle.dump(dic,f)

f.close()
# -------------------------反序列化
# import pickle
#
# f = open('序列化对象_pickle', 'rb')
#
# data = pickle.loads(f.read())  # 等价于data=pickle.load(f)
#
# print(data['age'])


