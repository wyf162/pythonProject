# -*- coding: utf-8 -*-
# @Time: 2024/6/20 10:04
# @Author: yfwang
# @File: 678D.py

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

tcn = 1
for _tcn_ in range(tcn):
    A, B, n, x = MI()
    if A == 1:
        y = x + n * B
        y %= mod
    else:
        y = pow(A, n, mod) * x + B * (pow(A, n, mod) - 1) * pow(A - 1, -1, mod)
        y %= mod
    print(y)

