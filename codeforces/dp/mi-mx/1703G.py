# -*- coding : utf-8 -*-
# @Time: 2024/1/6 19:34
# @Author: yefei.wang
# @File: 1703G.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
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
    n, k = MI()
    A = LI()
    dp = [[float('-inf') for _ in range(32)] for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(32):
            if j < 31:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (A[i] >> (j + 1)))
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + (A[i] >> j) - k)
            if j == 31:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
    ret = max(dp[-1])
    print(ret)
