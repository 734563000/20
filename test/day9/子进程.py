#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

from multiprocessing import Process
import time

def task(name):
    p=Process(target=time.sleep,args=(6,))
    p.start()
    print('%s is running' %name)
    time.sleep(5)
    print('%s is done'%name)


if  __name__ == '__main__':
    p=Process(target=task,args=('alex',))
    p.daemon=True
    p.start()
    time.sleep(1)
    print('主')