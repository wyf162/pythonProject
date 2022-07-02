# -*- coding : utf-8 -*-
# @Time: 2022/6/30 22:17
# @Author: yefei.wang
# @File: thread-02.py

import time
from threading import Thread

a = 0


def add():
    global a
    for i in range(100000):
        a += 1
        # time.sleep(0.0000001)


if __name__ == '__main__':
    ts = []
    for i in range(10):
        t = Thread(target=add)
        t.start()
        ts.append(t)

    for t in ts:
        t.join()

    print(a)
