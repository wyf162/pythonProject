# -*- coding : utf-8 -*-
# @Time: 2023/11/11 19:17
# @Author: yefei.wang
# @File: D.py
import math
import os
import sys

# 请在此输入您的代码
sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m, q = MI()

mtx = [LI() for _ in range(n)]
dp = [[[-1, -1, -1, -1] for j in range(m + 1)] for i in range(n + 1)]

dp[1][1][q] = mtx[0][0]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        for k in range(q, -1, -1):
            if dp[i - 1][j][k] >= 0:
                if math.gcd(mtx[i - 1][j - 1], mtx[i - 2][j - 1]) > 1:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + mtx[i - 1][j - 1])
                elif k > 0:
                    dp[i][j][k - 1] = max(dp[i][j][k - 1], dp[i - 1][j][k] + mtx[i - 1][j - 1])

            if dp[i][j - 1][k] >= 0:
                if math.gcd(mtx[i - 1][j - 1], mtx[i - 1][j - 2]) > 1:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k] + mtx[i - 1][j - 1])
                elif k > 0:
                    dp[i][j][k - 1] = max(dp[i][j][k - 1], dp[i][j - 1][k] + mtx[i - 1][j - 1])
rst = max(dp[-1][-1])
print(rst)
