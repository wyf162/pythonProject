# -*- coding: utf-8 -*-
# @Time: 2024/2/20 13:14
# @Author: yfwang
# @File: 1928C.py
# https://codeforces.com/problemset/problem/1928/C

import math
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()

for _tcn_ in range(tcn):
    n, x = MI()
    ret = set()
    if (n + x) % 2 == 0:
        ret.add((n + x) // 2)

    z = n - x
    for y in range(1, int(math.sqrt(z)) + 1):
        if z % y == 0:
            if y % 2 == 0:
                k1 = (y + 2) // 2
                if k1 >= x:
                    ret.add(k1)
            if (z // y) % 2 == 0:
                k2 = ((z // y) + 2) // 2
                if k2 >= x:
                    ret.add(k2)

    z = n + x - 2
    for y in range(1, int(math.sqrt(z)) + 1):
        if z % y == 0:
            if y % 2 == 0:
                k1 = (y + 2) // 2
                if k1 >= x:
                    ret.add(k1)
            if (z // y) % 2 == 0:
                k2 = ((z // y) + 2) // 2
                if k2 >= x:
                    ret.add(k2)

    print(len(ret))
