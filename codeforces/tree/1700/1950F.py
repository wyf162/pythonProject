# -*- coding: utf-8 -*-
# @Time: 2024/6/19 9:06
# @Author: yfwang
# @File: 1950F.py
# trees

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
    a, b, c = MI()
    if c != a + 1:
        print(-1)
    else:
        h = a.bit_length()
        tot = (1 << h) - 1
        bu = tot - a
        b -= bu
        while b > 0:
            b -= c
            h += 1
        print(h)

