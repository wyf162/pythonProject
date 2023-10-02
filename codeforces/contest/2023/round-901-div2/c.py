# -*- coding : utf-8 -*-
# @Time: 2023/9/30 23:44
# @Author: yefei.wang
# @File: c.py

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
    n, m = MI()
    x, y = divmod(n, m)
    if y == 0:
        print(0)
        continue

    k = m // math.gcd(m, y)
    if bin(k).count('1') > 1:
        print(-1)
        continue

    i = 1
    knife = 0
    while y:
        knife += y
        y *= 2
        y %= m
    print(knife)
