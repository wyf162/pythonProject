# -*- coding : utf-8 -*-
# @Time: 2024/6/14 20:39
# @Author: yefei.wang
# @File: E.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 2
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    parent = LGMI()
    tree = [[] for _ in range(n)]
    for x, fa in enumerate(parent):
        if fa >= 0:
            tree[fa].append(x)

    f = [0] * n
    g = [0] * n

    stk = [0]
    dfs = []
    while stk:
        x = stk.pop()
        dfs.append(x)
        for y in tree[x]:
            stk.append(y)
            f[y] += f[x] + A[x]

    for x in dfs[::-1]:
        fa = parent[x]
        if fa >= 0:
            g[fa] += g[x] + A[x]

    # print(f)
    # print(g)

    C = [0] * n
    for i in range(n):
        if f[i] >= A[i] >= g[i]:
            C[i] = 1
    h1 = [0] * n
    for x in dfs[::-1]:
        fa = parent[x]
        if fa >= 0:
            h1[fa] += h1[x] + C[x]

    # print(sum(C))

    B = [0] * n
    for i in range(n):
        if f[i] >= A[i] and A[i] < g[i]:
            B[i] = 1

    h2 = [0] * n
    for x in dfs:
        for y in tree[x]:
            stk.append(y)
            h2[y] += h2[x] + B[x]

    tot = sum(C)
    D = [h2[i] - h1[i] for i in range(n)] + [0]
    ans = max(D) + tot
    print(ans)
