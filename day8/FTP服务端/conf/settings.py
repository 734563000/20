#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHARE_DIR=os.path.join(BASE_DIR,'ROOT')
DB_DIR=os.path.join(BASE_DIR,'db')

HOST = "0.0.0.0"
PORT = 8081
Current_user=[]