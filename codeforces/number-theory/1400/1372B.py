# -*- coding: utf-8 -*-
# @Time: 2024/7/22 9:04
# @Author: yfwang
# @File: 1372B.py

import math
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    # a + b = n
    # let lcm(a, b) min
    a = 1
    b = n - 1
    c = n - 1

    for x in range(2, math.isqrt(n) + 1):
        if n % x:
            continue
        y = n // x
        z = x * (y - 1)
        if z < c:
            a, b, c = x, x * (y - 1), x * (y - 1)
        z = (x - 1) * y
        if z < c:
            a, b, c = y, (x - 1) * y, (x - 1) * y

    print(a, b)
