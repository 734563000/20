#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio
# import configparser,os
# from conf import settings
#
# config = configparser.ConfigParser()
# config.read(os.path.join(settings.DB_DIR, 'db.ini'))
# username = config.sections()
#
# print(config.get(username,'passwd'))


# msg = '''
#     get:    下载
#     put:    上传
#     pwd:    查看当前目录
#     cd:     切换目录
#     rm:     删除
#     mv:     移动
#     cp:     复制
#     mkdir:  创建目录
#     logout:退出
#
#     For example : get a.txt
# '''
# print(type(msg))
import time
data_size=1025
recv_size=0
while recv_size < data_size:
    time.sleep(0.1) #模拟数据的传输延迟
    recv_size+=1024 #每次收1024

    percent=recv_size/data_size #接收的比例
    progress(percent,width=70) #进度条的宽度70


progress_test()