#!/usr/bin/envpython
# -*- coding:utf-8-*-
# Author:Eio

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
# print(base_dir)

from core import main



#主要启动程序
if __name__ == '__main__':
    main.run()