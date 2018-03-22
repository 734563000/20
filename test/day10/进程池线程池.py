#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time,random,os

def task(n):
    print('%s is running' %os.getpid())
    time.sleep(random.randint(1,3))
    return n**2

def handle(res):
    res = res.result()
    print('handle res %s'%res)

if __name__ == '__main__':
    pool=ProcessPoolExecutor(2)

    for i in range(5):
        obj=pool.submit(task,i)
        obj.add_done_callback(handle)

    pool.shutdown(wait=True)
    print('主')