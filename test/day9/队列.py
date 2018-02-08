
#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio
from multiprocessing import Queue

q=Queue(3)

q.put('first')
q.put('2')
q.put('3')

try:
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get(timeout=1))
except Exception as e:
    print(e)