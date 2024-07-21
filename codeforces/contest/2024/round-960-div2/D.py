# -*- coding : utf-8 -*-
# @Time: 2024/7/20 23:58
# @Author: yefei.wang
# @File: D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
    A = LI()
    dp = [0] * (n + 1)

    mi = [n, n]
    for i in range(n):
        dp[i + 1] = dp[i] + 1
        if A[i] == 0:
            dp[i + 1] = min(dp[i + 1], dp[i])
        if A[i] <= 2:
            dp[i + 1] = min(dp[i + 1], i + 1 + mi[i % 2])

        if A[i] <= 2:
            mi[1 - i % 2] = min(mi[1 - i % 2], dp[i] - i - 1)
        elif A[i] > 4:
            mi[0] = mi[1] = n

    print(dp[n])
