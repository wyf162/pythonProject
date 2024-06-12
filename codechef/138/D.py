# -*- coding : utf-8 -*-
# @Time: 2024/6/12 22:53
# @Author: yefei.wang
# @File: D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 0x3f3f3f3f

tcn = I()
for _tcn_ in range(tcn):
    a = I()
    if a == 2:
        print(12, 16)
    else:
        b = 2 * a
        c = a * a
        print(b, c)
