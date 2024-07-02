# -*- coding: utf-8 -*-
# @Time: 2024/7/2 15:07
# @Author: yfwang
# @File: 1932F.py

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
inf = 10 ** 9

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    segments = [LI() for _ in range(m)]

    SUM = [0] * (n + 5)
    MAX = [i for i in range(n+5)]
    for x1, x2 in segments:
        SUM[x1] += 1
        SUM[x2+1] -= 1
        MAX[x1] = max(MAX[x1], x2)

    for i in range(1, n + 5):
        SUM[i] += SUM[i-1]
        MAX[i] = max(MAX[i], MAX[i-1])

    DP = [0] * (n + 5)
    for i in range(n + 5):
        DP[i] = max(DP[i], DP[i-1])
        if i < n + 4:
            DP[MAX[i] + 1] = max(DP[MAX[i]+1], DP[i] + SUM[i])
    print(DP[-1])
