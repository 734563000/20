#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import os,sys
# from core import main
from conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# if __name__ == '__main__':
#     main.run()



import configparser

config=configparser.ConfigParser()
config.read(os.path.join(settings.CONFIG_DIR,'host.ini'),encoding='utf-8')

# res=config.sections()
# print(res)
#
# options=config.options('group')
# print(options)

val=config.get('group','test')
print(type(val),val)
val_new = eval(val)
print(type(val_new),val_new)



