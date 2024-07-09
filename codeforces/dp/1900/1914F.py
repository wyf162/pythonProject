# -*- coding: utf-8 -*-
# @Time: 2024/7/9 13:22
# @Author: yfwang
# @File: 1914F.py
# tree

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    tree = [[] for _ in range(n)]
    parent = [-1] * n
    for i, fa in enumerate(LGMI(), start=1):
        tree[fa].append(i)
        parent[i] = fa

    # for i in range(n):
    #     for j in tree[i]:
    #         print(i, j)

    stk = [0]
    dfs = []
    while stk:
        x = stk.pop()
        dfs.append(x)
        for y in tree[x]:
            stk.append(y)

    sz = [0] * n
    for x in dfs[::-1]:
        sz[x] += 1
        fa = parent[x]
        if fa >= 0:
            sz[fa] += sz[x]
    # print(sz)

    dp = [0] * n
    for x in dfs[::-1]:
        child = []
        tot0 = 0
        for y in tree[x]:
            child.append((sz[y], y))
            tot0 += sz[y]
        child.sort()
        if not child:
            continue
        if child[-1][0] * 2 <= tot0:
            dp[x] = tot0
            dp[x] = dp[x] // 2 * 2
        else:
            v = tot0 - child[-1][0]
            dp[x] = min(tot0, v * 2 + dp[child[-1][1]])
            dp[x] = dp[x] // 2 * 2

    print(dp[0] // 2)





