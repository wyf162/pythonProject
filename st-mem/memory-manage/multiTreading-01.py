# -*- coding : utf-8 -*-
# @Time: 2022/6/24 23:11
# @Author: yefei.wang
# @File: multiTreading-00.py

import time
from threading import Thread


def count():
    print('One')
    time.sleep(1)
    print('Two')


def main():

    t_list = []
    for _ in range(3):
        t_list.append(Thread(target=count))
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()


if __name__ == '__main__':
    import time
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds")