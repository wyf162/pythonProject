# -*- coding: utf-8 -*-
# @Time: 2024/6/24 8:56
# @Author: yfwang
# @File: 1759E.py

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
    n, H = MI()
    A = LI()
    A.sort()

    i, c, h = 0, 0, H
    ans = 0
    while i < n:
        a = A[i]
        if a < h:
            h += a // 2
            i += 1
        else:
            if c == 0:
                h *= 2
            elif c == 1:
                h *= 2
            elif c == 2:
                h *= 3
            else:
                break
            c += 1
    ans = max(ans, i)

    i, c, h = 0, 0, H
    while i < n:
        a = A[i]
        if a < h:
            h += a // 2
            i += 1
        else:
            if c == 0:
                h *= 2
            elif c == 1:
                h *= 3
            elif c == 2:
                h *= 2
            else:
                break
            c += 1
    ans = max(ans, i)

    i, c, h = 0, 0, H
    while i < n:
        a = A[i]
        if a < h:
            h += a // 2
            i += 1
        else:
            if c == 0:
                h *= 3
            elif c == 1:
                h *= 2
            elif c == 2:
                h *= 2
            else:
                break
            c += 1
    ans = max(ans, i)
    print(ans)
