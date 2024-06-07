# -*- coding: utf-8 -*-
# @Time: 2024/4/15 15:32
# @Author: yfwang
# @File: 1463D.py
# https://codeforces.com/contest/1463/problem/D

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
    N = I()
    B = set(LI())

    ma = 0
    small = 0
    for i in range(1, 2 * N + 1):
        if i in B:
            small += 1
        else:
            if small > 0:
                small -= 1
                ma += 1

    mi = N
    big = 0
    for i in range(2 * N, 0, -1):
        if i in B:
            big += 1
        else:
            if big > 0:
                big -= 1
                mi -= 1

    print(ma - mi + 1)
