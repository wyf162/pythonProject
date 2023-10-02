# -*- coding : utf-8 -*-
# @Time: 2023/9/30 22:22
# @Author: yefei.wang
# @File: ee.py
"""
考察

やるかやらないかの二択が100個
愚直だと O(2^100)
こういうやるかやらないかのときはDP

K, P が5以下

dp[i][j][k][l][m] = v
"""

from collections import defaultdict
N, K, P = map(int, input().split())
C = []
A = []
for _ in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

dp = defaultdict(int)
dp[tuple(0 for _ in range(K))] = 0
for i in range(N):
    for ok, ov in dp.copy().items():
        nk = tuple(min(k+A[i][j], P) for j, k in enumerate(ok))
        if nk not in dp or dp[nk] > ov + C[i]:
            dp[nk] = ov + C[i]
ak = tuple(P for _ in range(K))
print(-1 if ak not in dp else dp[ak])

