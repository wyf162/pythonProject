# -*- coding : utf-8 -*-
# @Time: 2024/6/29 11:24
# @Author: yefei.wang
# @File: 1955F.py

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

X, Y, Z = 201, 201, 201


def idx(i, j, k):
    return i * Y * Z + (j * Z + k)


N = X * Y * Z
dp = [0] * N
for i in range(X):
    for j in range(Y):
        for k in range(Z):
            i1 = idx(i, j, k)
            if i > 0:
                i2 = idx(i - 1, j, k)
                if i % 2 == j % 2 == k % 2:
                    dp[i1] = max(dp[i1], dp[i2] + 1)
                else:
                    dp[i1] = max(dp[i1], dp[i2])
            if j > 0:
                i2 = idx(i, j - 1, k)
                if i % 2 == j % 2 == k % 2:
                    dp[i1] = max(dp[i1], dp[i2] + 1)
                else:
                    dp[i1] = max(dp[i1], dp[i2])
            if k > 0:
                i2 = idx(i, j, k - 1)
                if i % 2 == j % 2 == k % 2:
                    dp[i1] = max(dp[i1], dp[i2] + 1)
                else:
                    dp[i1] = max(dp[i1], dp[i2])

tcn = I()
for _tcn_ in range(tcn):
    cnt = LI()
    i1 = idx(*cnt[:3])
    ans = dp[-1] + cnt[3] // 2
    print(ans)
