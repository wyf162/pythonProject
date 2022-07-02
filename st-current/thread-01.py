# -*- coding : utf-8 -*-
# @Time: 2022/6/30 20:47
# @Author: yefei.wang
# @File: thread-01.py
import time
import random

from threading import Thread

from threading import Thread
import time

a = 0  # global variable


def thread1(threadname):
    global a
    for k in range(10):
        print("{} {}".format(threadname, a))
        time.sleep(0.1)
        if a == 5:
            a += 100


def thread2(threadname):
    global a
    for k in range(10):
        print("{} {}".format(threadname, a))
        a += 1
        time.sleep(0.1)


if __name__ == '__main__':
    thread1 = Thread(target=thread1, args=("Thread-1",))
    thread2 = Thread(target=thread2, args=("Thread-2",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
