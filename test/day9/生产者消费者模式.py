#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

from multiprocessing import Process,JoinableQueue
import time,random

def producer(name,food,q):
    for i in range(3):
        res = '%s%s' %(food,i)
        time.sleep(random.randint(1,3))
        q.put(res)
        print('厨师[%s]生产了<%s>'%(name,res))


def consumer(name,q):
    while True:
        res=q.get()
        time.sleep(random.randint(1,3))
        print('吃货[%s]吃了<%s>'%(name,res))
        q.task_done()

if __name__ == '__main__':
    q=JoinableQueue()

    p1=Process(target=producer,args=('egon','泔水',q))
    p2=Process(target=producer,args=('egon1','骨头',q))

    c1=Process(target=consumer,args=('11',q))
    c2=Process(target=consumer,args=('22',q))
    c3=Process(target=consumer,args=('33',q))
    c1.daemon=True
    c2.daemon=True
    c3.daemon=True


    p1.start()
    p2.start()
    c1.start()
    c2.start()
    c3.start()

    p1.join()
    p2.join()
    q.join()
    print('主')