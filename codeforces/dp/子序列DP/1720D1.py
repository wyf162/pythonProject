# -*- coding : utf-8 -*-
# @Time: 2024/2/5 21:40
# @Author: yefei.wang
# @File: 1720D1.py

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
    n = I()
    A = LI()

    E = [[] for i in range(n)]
    for i in range(n):
        a = A[i]
        for j in range(i + 1, min(n, i + 256)):
            if a ^ j < A[j] ^ i:
                E[i].append(j)

    dp = [0] * n
    for i in range(n):
        for to in E[i]:
            dp[to] = max(dp[to], dp[i] + 1)
    print(max(dp) + 1)
