# -*- coding : utf-8 -*-
# @Time: 2023/10/11 0:19
# @Author: yefei.wang
# @File: 1359C.py

import sys
from collections import deque

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    h, c, t = MI()
    if t >= h:
        print('1')
        continue
    elif t * 2 <= c + h:
        print('2')
        continue


