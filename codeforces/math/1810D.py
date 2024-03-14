# -*- coding: utf-8 -*-
# @Time: 2024/3/14 15:54
# @Author: yfwang
# @File: 1810D.py
# https://codeforces.com/problemset/problem/1810/D

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    n = I()
    events = [LI() for _ in range(n)]
    mi, mx = 1, 1 << 63
    for event in events:
        if event[0] == 1:
            _, a, b, n = event
            if n >= 2:
                h1 = (a - b) * (n - 2) + a + 1
                h2 = (a - b) * (n - 1) + a
            else:
                h1 = 1
                h2 = a
            if max(mi, h1) <= min(mx, h2):
                mi = max(mi, h1)
                mx = min(mx, h2)
                print(1, end=' ')
            else:
                print(0, end=' ')
        elif event[0] == 2:
            _, a, b = event
            d1 = max((mi - a + a - b - 1) // (a - b), 0) + 1
            d2 = max((mx - a + a - b - 1) // (a - b), 0) + 1

            if d1 == d2:
                print(d1, end=' ')
            else:
                print(-1, end=' ')
    print()
