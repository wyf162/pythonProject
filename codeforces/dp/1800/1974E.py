# -*- coding: utf-8 -*-
# @Time: 2024/6/24 16:28
# @Author: yfwang
# @File: 1974E.py
# knapsack

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
inf = 10 ** 18

tcn = I()
for _tcn_ in range(tcn):
    m, x = MI()
    ops = [LI() for _ in range(m)]

    mh = sum(h for c, h in ops)
    dp = [0] + [inf] * mh
    for i in range(m):
        for j in range(mh, ops[i][1] - 1, -1):
            if dp[j - ops[i][1]] + ops[i][0] <= i * x:
                dp[j] = min(dp[j], dp[j - ops[i][1]] + ops[i][0])
    for i in range(mh, -1, -1):
        if dp[i] < inf:
            print(i)
            break
