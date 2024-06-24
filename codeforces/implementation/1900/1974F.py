# -*- coding: utf-8 -*-
# @Time: 2024/6/24 15:00
# @Author: yfwang
# @File: 1974F.py
# sortings

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
    a, b, n, m = MI()
    points = [LI() + [i] for i in range(n)]
    ver = sorted(points, key=lambda x: x[0])
    hor = sorted(points, key=lambda x: x[1])
    x1, x2 = 1, a
    y1, y2 = 1, b
    i1, i2 = 0, n - 1
    j1, j2 = 0, n - 1

    unvis = [1] * n
    alice = bob = 0
    for op in range(m):
        c = 0
        typ, k = input().split()
        k = int(k)
        if typ == 'U':
            x1 += k
            while i1 <= i2 and ver[i1][0] < x1:
                i = ver[i1][2]
                c += unvis[i]
                unvis[i] = 0
                i1 += 1
        elif typ == 'D':
            x2 -= k
            while i1 <= i2 and ver[i2][0] > x2:
                i = ver[i2][2]
                c += unvis[i]
                unvis[i] = 0
                i2 -= 1
        elif typ == 'L':
            y1 += k
            while j1 <= j2 and hor[j1][1] < y1:
                i = hor[j1][2]
                c += unvis[i]
                unvis[i] = 0
                j1 += 1
        elif typ == 'R':
            y2 -= k
            while j1<=j2 and hor[j2][1] > y2:
                i = hor[j2][2]
                c += unvis[i]
                unvis[i] = 0
                j2 -= 1
        if op % 2 == 0:
            alice += c
        else:
            bob += c

    print(alice, bob)
