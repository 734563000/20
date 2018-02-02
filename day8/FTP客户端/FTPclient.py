#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import socket,json,struct,sys,os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

ROOT_DIR = os.path.join(BASE_DIR,'ROOT')

HOST = "127.0.0.1"
PORT = 8081



# client = socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((HOST, PORT))

class FTPClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((HOST,PORT))

    def interactive(self,user):
        print('welcome %s !' %user)
        while True:
            cmd=input('>>(h for help): ').strip()
            if not cmd:continue
            params=cmd.split()
            # if len(params) ==1:continue
            if hasattr(self, params[0]):
                func = getattr(self, params[0])
                params.append(user)
                func(params)
            else:
                print('cmd not exists !')
                continue

    def get(self,cmd):
        print('in get',cmd)
        while True:
            # cmd=input('>>: ').strip()
            # if not cmd:continue
            # self.client.send(cmd.encode('utf-8'))
            cmd_json = json.dumps(cmd)
            self.client.send(cmd_json.encode('utf-8'))
            # print('命令发送')
            #1、先接收报头的长度
            headers_size=struct.unpack('i',self.client.recv(4))[0]
            if headers_size == 0:
                print('文件不存在!')
                break
            # print('接受爆头长度')
            #2、再收报头
            # print('接受报文')
            headers_bytes=self.client.recv(headers_size)
            headers_json=headers_bytes.decode('utf-8')
            headers_dic=json.loads(headers_json)
            # print('========>',headers_dic)
            total_size=headers_dic['filesize']

            #3、再收命令的结果
            filepath = os.path.join(ROOT_DIR,headers_dic['filename'])
            recv_size=0
            data=b''
            while recv_size < total_size:
                recv_data=self.client.recv(1024)
                data+=recv_data
                recv_size+=len(recv_data)
            with open(filepath,'w') as f:
                f.write(data.decode('utf-8'))
            print('接受成功')
            break
        # self.client.close()

    def login(self):
        while True:
            username=input('username>>: ').strip()
            if not username: continue
            passwd=input('passwd>>: ').strip()
            if not passwd:continue
            break
        user_dic = [username,passwd]
        user_json = json.dumps(user_dic)
        user_bytes = user_json.encode('utf-8')
        self.client.send(user_bytes)
        data = self.client.recv(1024)
        return json.loads(data.decode('utf-8'))
        # print(data)
        self.client.close()

    def logout(self,cmd):
        exit('Bye bye!')

    def ls(self,cmd):
        cmd_json = json.dumps(cmd)
        self.client.send(cmd_json.encode('utf-8'))
        ls_bytes = self.client.recv(1024)
        ls_json = ls_bytes.decode('utf-8')
        headers_dic = json.loads(ls_json)
        print(headers_dic)

    def h(self,cmd):
        print('in h')
        cmd_json = json.dumps(cmd)
        self.client.send(cmd_json.encode('utf-8'))
        recv_data = self.client.recv(1024)
        print(recv_data.decode('utf-8'))





if __name__ == "__main__":
    ftp = FTPClient()
    while True:
        res=ftp.login()
        if res[0] == '1':
            ftp.interactive(res[1])  # 交互
        else:
            print('username or passwd error !')