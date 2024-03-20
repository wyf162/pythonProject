# -*- coding: utf-8 -*-
# @Time: 2024/3/19 17:25
# @Author: yfwang
# @File: E.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
    p = LI()
    if n == 1:
        print(0)
    else:
        pos = p.index(x)
        p[0], p[pos] = p[pos], p[0]
        l, r = 0, n
        while r - l > 1:
            m = (l + r) // 2
            if p[m] <= x:
                l = m
            else:
                r = m
        if p[l] == x:
            print(1)
            print(1, pos + 1)
        else:
            print(2)
            print(1, pos + 1)
            print(1, l + 1)
