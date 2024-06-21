# -*- coding: utf-8 -*-
# @Time: 2024/6/21 9:30
# @Author: yfwang
# @File: 1151D.py

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

tcn = 3
for _tcn_ in range(tcn):
    n = I()
    C = []
    tot = 0
    for i in range(n):
        a, b = MI()
        tot += b * n - a
        C.append(a - b)
    C.sort(reverse=True)
    for i, c in enumerate(C, start=1):
        tot += c * i
    print(tot)