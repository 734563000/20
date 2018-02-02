#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import socket
import os
import json
import struct
import configparser
from conf import settings

# SHARE_DIR=r'F:\Python周末20期\day8\08 上传下载文件\SHARE'

class FtpServer:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((self.host,self.port))
        self.server.listen(5)

    def serve_forever(self):
        while True:
            try:
                print('in serve_forever')
                data = self.conn.recv(1024)  #params_json.encode('utf-8')
                if not data:break
                params=json.loads(data.decode('utf-8')) #params=['get','a.txt']
                cmd=params[0] #
                if hasattr(self,cmd):
                    func=getattr(self,cmd)
                    func(params)
                else:
                    print('cmd not exists !')
            except ConnectionResetError:
                break
        self.conn.close()

    def get(self,params): #params=['get','a.txt']
        print('in get')
        if len(params) < 3:
            headers_bytes = {}
            self.conn.send(struct.pack('i', len(headers_bytes)))
            return
        username=params[2]
        filename=params[1] #filename='a.txt'
        filepath = os.path.join(settings.SHARE_DIR, username, filename)
        if os.path.exists(filepath):
            #1、制作报头
            headers = {
                'filename': filename,
                'md5': '123sxd123x123',
                'filesize': os.path.getsize(filepath)
            }

            headers_json = json.dumps(headers)
            headers_bytes = headers_json.encode('utf-8')

            #2、先发报头的长度
            self.conn.send(struct.pack('i',len(headers_bytes)))
            # print('发送报文长度')
            #3、发送报头
            self.conn.send(headers_bytes)
            # print('发送报头')

            #4、发送真实的数据
            # print('发送数据')
            with open(filepath,'rb') as f:
                for line in f:
                    self.conn.send(line)
        # else:
        #     headers_bytes = {}
        #     self.conn.send(struct.pack('i', len(headers_bytes)))

    def put(self,params):
        filename=params[1] #filename='a.txt'
        filepath=os.path.join(settings.SHARE_DIR,filename) #
        if os.path.exists(filepath):
            print('file allready exists !')
            return
        # #1、制作报头
        # headers = {
        #     'filename': filename,
        #     'md5': '123sxd123x123',
        #     'filesize': os.path.getsize(filepath)
        # }
        #
        # headers_json = json.dumps(headers)
        # headers_bytes = headers_json.encode('utf-8')
        #
        # #2、先发报头的长度
        # self.conn.send(struct.pack('i',len(headers_bytes)))
        #
        # #3、发送报头
        # self.conn.send(headers_bytes)
        #
        # #4、发送真实的数据
        # with open(filepath,'rb') as f:
        #     for line in f:
        #         self.conn.send(line)

    def cd(self):
        pass

    def pwd(self):
        pass

    def mkdir(self):
        pass

    def cp(self):
        pass

    def mv(self):
        pass

    def rm(self):
        pass

    def ls(self,params):
        print( 'ls')
        username=params[2]
        filepath = os.path.join(settings.SHARE_DIR,username)
        print(os.listdir(filepath))



    def login(self):
        print('waiting for login...')
        while True:
            self.conn, self.client_addr = self.server.accept()  # (conn,client_addr)
            print(self.client_addr)
            while True:
                try:
                    data = self.conn.recv(1024)
                    if not data: break
                    user_dic = json.loads(data.decode('utf-8'))# 1024
                    config = configparser.ConfigParser()
                    config.read(os.path.join(settings.DB_DIR,'db.ini'))
                    username = config.sections()
                    if user_dic[0] in username:
                        if user_dic[1] == config.get(user_dic[0],'passwd'):
                            res = ['1',user_dic[0]]
                            res_json = json.dumps(res)
                            res_bytes = res_json.encode('utf-8')
                            self.conn.send(res_bytes)
                            self.serve_forever()
                            break
                        else:
                            res1 = ['0']
                            res1_json = json.dumps(res1)
                            res1_bytes = res1_json.encode('utf-8')
                            self.conn.send(res1_bytes)
                            continue
                    else:
                        res2 = ['0']
                        res2_json = json.dumps(res2)
                        res2_bytes = res2_json.encode('utf-8')
                        self.conn.send(res2_bytes)
                        continue
                except ConnectionResetError:
                    break
            self.conn.close()
        self.server.close()

    def h(self,cmd):
        msg = '''
    ls:     查看当前文件
    get:    下载
    put:    上传
    pwd:    查看当前目录
    cd:     切换目录
    rm:     删除
    mv:     移动
    cp:     复制
    mkdir:  创建目录
    logout: 退出

    For example : get a.txt
        '''

        self.conn.send(msg.encode('utf-8'))