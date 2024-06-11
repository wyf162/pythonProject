# -*- coding: utf-8 -*-
# @Time: 2024/6/11 15:44
# @Author: yfwang
# @File: I.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    stk = [(0, -1)]
    parent = [-1] * n
    dfs = []
    while stk:
        x, fa = stk.pop()
        dfs.append(x)
        for y in g[x]:
            if y != fa:
                stk.append((y, x))
                parent[y] = x

    dp = [[0 for _ in range(n)] for _ in range(3)]

    for x in dfs[::-1]:
        dp[0][x] = dp[1][x] = 1

        for y in g[x]:
            if y == parent[x]:
                continue
            dp[0][x] *= dp[0][y] + dp[1][y] + dp[2][y]
            dp[0][x] %= mod
            dp[1][x] *= dp[0][y]
            dp[1][x] %= mod

        left = [1]
        for y in g[x]:
            if y == parent[x]:
                continue
            left.append(left[-1] * dp[0][y])
            left[-1] %= mod
        right = [1]
        for y in g[x][::-1]:
            if y == parent[x]:
                continue
            right.append(right[-1] * dp[0][y])
            right[-1] %= mod
        right = right[::-1]

        i1 = 0
        for y in g[x]:
            if y == parent[x]:
                continue
            dp[2][x] += dp[1][y] * left[i1] * right[i1 + 1]
            dp[2][x] %= mod
            i1 += 1

    ans = dp[0][0] + dp[1][0] + dp[2][0]
    print(ans)
