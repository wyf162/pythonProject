# -*- coding : utf-8 -*-
# @Time: 2024/5/23 21:49
# @Author: yefei.wang
# @File: 510D.py
# https://codeforces.com/contest/510/problem/D
# 裴蜀定理

import math
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
inf = 10 ** 10

tcn = 4
for _tcn_ in range(tcn):
    n = I()
    L = LI()
    C = LI()
    ans = inf
    dp = [dict() for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for k in dp[i]:
            g = math.gcd(k, L[i])
            if g in dp[i + 1]:
                dp[i + 1][g] = min(dp[i + 1][g], dp[i][k] + C[i])
            else:
                dp[i + 1][g] = dp[i][k] + C[i]
        for k in dp[i]:
            if k in dp[i + 1]:
                dp[i + 1][k] = min(dp[i + 1][k], dp[i][k])
            else:
                dp[i + 1][k] = dp[i][k]

    if 1 in dp[-1]:
        print(dp[-1][1])
    else:
        print(-1)
