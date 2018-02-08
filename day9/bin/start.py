#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import os,sys
import configparser
from core import main
from conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# config=configparser.ConfigParser()
# config.read(os.path.join(settings.CONFIG_DIR,'host.ini'),encoding='utf-8')

if __name__ == '__main__':
    while True:
        cmd = input("cmd >>: ").strip()
        if cmd == 'exit':
            break
        if len(cmd) == 0 :
            continue
        cmd_dic = main.cmd_parse(cmd)
        print(cmd_dic)
        # if len(cmd_dic) == 0:
        #     continue
        # res=main.cmd_action(cmd_dic)


