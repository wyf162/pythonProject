# -*- coding : utf-8 -*-
# @Time: 2023/11/17 22:35
# @Author: yefei.wang
# @File: C.py

import sys

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    if n % 3 in [2, 1]:
        print('First')
    else:
        print('Second')
