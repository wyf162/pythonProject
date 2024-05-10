# -*- coding: utf-8 -*-
# @Time: 2024/5/10 16:47
# @Author: yfwang
# @File: 1574D.py

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = []
    for _ in range(n):
        _, *a = LI()
        A.append(a)
    m = I()
    B = [LI() for _ in range(m)]


