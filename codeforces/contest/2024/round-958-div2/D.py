# -*- coding : utf-8 -*-
# @Time: 2024/7/15 22:54
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
inf = 10 ** 18

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()

    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    stk = [0]
    dfs = []
    parent = [-1] * n
    depth = [0] * n
    while stk:
        x = stk.pop()
        dfs.append(x)
        for y in g[x]:
            if parent[x] != y:
                stk.append(y)
                parent[y] = x
                depth[y] = depth[x] + 1

    dp = [[0] * 20 for _ in range(n)]
    for x in range(n):
        for i in range(20):
            dp[x][i] = (i + 1) * A[x]

    for x in dfs[::-1]:
        fa = parent[x]
        if fa < 0:
            continue

        for i in range(20):
            mi = inf
            for j in range(20):
                if i == j:
                    continue
                mi = min(mi, dp[x][j])
            dp[fa][i] += mi

    ans = min(dp[0])
    print(ans)
