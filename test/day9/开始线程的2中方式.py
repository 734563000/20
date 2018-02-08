#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

from threading import Thread
import time,random

class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s is piaoing'% self.name)
        time.sleep(random.randint(1,3))
        print('%s is piao wan le!'%self.name)

if __name__ == '__main__':
    t1 = MyThread('alex')
    t1.start()
    print('主')