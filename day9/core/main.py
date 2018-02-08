#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import paramiko,os
from conf import settings


transport = paramiko.Transport(('192.168.21.117', 22))
transport.connect(username='root', password='123456')


def run():
    cmd = input(">>>:").strip()






