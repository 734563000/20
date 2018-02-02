#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import os,sys
from core import main
from conf import settings



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


if __name__ == '__main__':
    server=main.FtpServer(settings.HOST,settings.PORT)
    server.login()
    # server.serve_forever()
