# -*- coding : utf-8 -*-
# @Time: 2023/9/30 23:15
# @Author: yefei.wang
# @File: a.py

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
    a, b, n = MI()
    x = LI()

    for i in range(n):
        b += min(a-1, x[i])

    print(b)
