# -*- coding: utf-8 -*-
# @Time: 2024/3/18 9:29
# @Author: yfwang
# @File: 870C.py
# https://codeforces.com/problemset/problem/870/C

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
    for _ in range(I()):
        n = I()
        if n <= 3:
            print(-1)
            continue
        c, k = n // 4, n % 4
        if k == 2 or k == 0:
            print(c)
        elif k == 1:
            if c >= 2:
                print(c - 1)
            else:
                print(-1)
        elif k == 3:
            if c >= 3:
                print(c - 1)
            else:
                print(-1)
