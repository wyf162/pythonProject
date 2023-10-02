# -*- coding : utf-8 -*-
# @Time: 2023/9/30 23:25
# @Author: yefei.wang
# @File: b.py

import math
import os
import sys
from collections import Counter, deque

BUFSIZE = 8192
MOD = 10 ** 9 + 7
MODD = 998244353
inf = float('inf')
sys.setrecursionlimit(10 ** 6)

# sys.stdin = open('./../input.txt', 'r')
# input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, m, k = MI()
    a = LI()
    b = LI()
    a.sort()
    b.sort()

    if k % 2 == 1:
        if a[0] > b[-1]:
            print(sum(a))
        else:
            print(sum(a[1:]) + b[-1])
    else:
        if a[0] > b[-1]:
            print(sum(a[:-1]) + b[0])
        else:
            mi = a.pop(0)
            mx = b.pop(-1)
            a.append(mx)
            b.append(mi)
            a.sort()
            b.sort()
            print(sum(a[:-1]) + b[0])
