# -*- coding : utf-8 -*-
# @Time: 2023/12/3 16:05
# @Author: yefei.wang
# @File: H.py

import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 998244353

tcn = 3

for _tnc_ in range(tcn):
    n = I()
    ab = [LI() for i in range(n)]
    MX = 0x3f3f3f3f
    dp = [[MX for j in range(n + 1)] for i in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][j] = min(dp[i - 1][j] + ab[i - 1][0], dp[i][j])
            if j - 1 >= 0:
                dp[i][j] = min(dp[i - 1][j - 1] - ab[i - 1][1], dp[i][j])

    for i in range(n + 1):
        if dp[n][i] <= 0:
            print(i)
            break
