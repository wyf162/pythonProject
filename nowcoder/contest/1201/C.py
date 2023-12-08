# -*- coding : utf-8 -*-
# @Time: 2023/12/1 19:15
# @Author: yefei.wang
# @File: C.py
import sys

sys.stdin = open('../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

mod = 998244353
N = 2 * 10 ** 5 + 5
f = [0] * N

dp = [[576, 24, 24],
      [24, 1, 1],
      [24, 1, 1], ]
X = [24, 1, 1]
for k in range(3, N):
    dpn = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0], ]
    for i in range(3):
        for j in range(3):
            for ni in range(3):
                if i == 1 and j == 2 and ni == 1:
                    continue
                dpn[j][ni] += dp[i][j] * X[ni]
                dpn[j][ni] %= mod

    dp = dpn
    f[k] = (pow(26, k, mod) - sum(sum(x) for x in dp)) % mod

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    print(f[n])
