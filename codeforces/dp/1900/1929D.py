# -*- coding: utf-8 -*-
# @Time: 2024/7/4 16:21
# @Author: yfwang
# @File: 1929D.py
# trees combinations

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
mod = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    stk = [0]
    parent = [-1] * n
    dfs = []
    while stk:
        x = stk.pop()
        dfs.append(x)
        for y in g[x]:
            if parent[x] != y:
                parent[y] = x
                stk.append(y)

    dp1 = [1] * n
    dp2 = [0] * n
    for x in dfs[::-1]:
        fa = parent[x]
        dp1[fa] = dp1[fa] * (1 + dp1[x]) % mod
        dp2[fa] = (dp2[fa] + dp1[x] + dp2[x]) % mod

    ans = dp1[0] + dp2[0] + 1
    ans %= mod
    print(ans)
