#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import paramiko,os,configparser
from conf import settings
import threading

config = configparser.ConfigParser()
config.read(os.path.join(settings.CONFIG_DIR,'host.ini'))

# transport = paramiko.Transport(('192.168.21.117', 22))
# transport.connect(username='root', password='123456')

def cmd_parse(cmd):
    #分析用户具体需要哪个功能,交给具体的功能去操作
    parse_func={
        'batch_run':batch_run_dic,
        'batch_scp':batch_scp_dic,
    }
    cmd_l=cmd.split()
    func=cmd_l[0]
    res=''
    if func in parse_func:
        res=parse_func[func](cmd_l)
    return res

def batch_run_dic(cmd_l):
    cmd_dic={
        'func':batch_run,
        '-h':[],
        '-g':[],
        '-cmd': [],
    }
    return handle_parse(cmd_l,cmd_dic)

def batch_scp_dic(cmd_l):
    cmd_dic={
        'func':batch_scp,
        '-h':[],
        '-g':[],
        '-action': [],
        '-local': [],
        '-remote': [],
    }
    return handle_parse(cmd_l,cmd_dic)

def handle_parse(cmd_l,cmd_dic):
    # 讲用户输入的数据转换成列表后填充到字典中
    tag=False
    for item in cmd_l:
        if item in cmd_dic:
            tag=True
            key=item
        if tag and item not in cmd_dic:
            cmd_dic[key].append(item)
    return cmd_dic

def batch_run(cmd_dic):
    group = cmd_dic['-g'][0].split(',')
    hosts = cmd_dic['-h'][0].split(',')
    group_options = config.options('group')
    for i in group:
        if i not in group_options:
            print('%s 组不存在 !' % i)
        else:
            ghosts = config.get('group',i).split(',')
            hosts.extend(ghosts)
    hosts = set(hosts)
    host_dic={}
    res = config.sections()
    for i in hosts:
        if i not in res:
            print('%s 主机不存在 !'%i)
        else:
            host_dic[i]={'ip':config.get(i,'ip'),'username':config.get(i,'username'), \
                          'passwd': config.get(i, 'passwd')}
    shell_cmd = ' '.join(cmd_dic['-cmd'])
    thread_list=[]
    for k in host_dic:
        host, port, username, password = host_dic[k]["ip"], host_dic[k]["port"], host_dic[k]["username"], host_dic[k][
            "passwd"]
        func = Remotehost(host, port, username, password, shell_cmd)  # 实例化类
        t = threading.Thread(target=func.run)  # 创建线程
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()  # 等待线程执行结果



def batch_scp(cmd_dic):
    group = cmd_dic['-g'][0].split(',')
    hosts = cmd_dic['-h'][0].split(',')
    group_options = config.options('group')
    for i in group:
        if i not in group_options:
            print('%s 组不存在 !' % i)
        else:
            ghosts = config.get('group',i).split(',')
            hosts.extend(ghosts)
    hosts = set(hosts)
    host_dic={}
    res = config.sections()
    for i in hosts:
        if i not in res:
            print('%s 主机不存在 !'%i)
        else:
            host_dic[i]={'ip':config.get(i,'ip'),'username':config.get(i,'username'), \
                          'passwd': config.get(i, 'passwd')}

def cmd_action(cmd_dic):
    return cmd_dic.get('func')(cmd_dic)

class Remotehost:
    # 远程操作主机
    def __init__(self, host, port, username, password, cmd):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.cmd = cmd

    def command(self):
        # 获取命令
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
        ssh.connect(hostname=self.host, port=self.port, username=self.username, password=self.password)  # 连接服务器
        stdin, stdout, stderr = ssh.exec_command(self.cmd)  # 获取命令结果
        res, err = stdout.read(), stderr.read()  # 三元运算
        result = res if res else err
        print("[%s]".center(50, "-") % self.host)
        print(result.decode())  # 打印输出
        ssh.close()




