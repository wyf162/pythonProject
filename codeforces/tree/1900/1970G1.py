# -*- coding: utf-8 -*-
# @Time: 2024/6/25 16:24
# @Author: yfwang
# @File: 1970G1.py

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
    n, m, c = MI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    size = [0] * n
    dfs = []
    stk = [(0, -1)]
    parent = [0] * n
    while stk:
        x, fa = stk.pop()
        parent[x] = fa
        dfs.append(x)
        for y in g[x]:
            if y == fa:
                continue
            stk.append((y, x))

    for x in dfs[::-1]:
        size[x] += 1
        fa = parent[x]
        if fa >= 0:
            size[fa] += size[x]
    # print(size)

    ans = n * n
    for x in range(1, n):
        tmp = size[x] * size[x] + (n - size[x]) * (n - size[x])
        ans = min(ans, tmp)
    print(ans)
