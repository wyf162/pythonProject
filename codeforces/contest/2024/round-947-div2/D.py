# -*- coding : utf-8 -*-
# @Time: 2024/5/25 23:46
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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a, b = GMI()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        x, y = GMI()
        g[x].append(y)
        g[y].append(x)

    fa = [-1] * n
    depth = [0] * n
    dfs = []
    stk = [a]
    fa[a] = n

    while stk:
        x = stk.pop()
        dfs.append(x)
        for y in g[x]:
            if fa[y] == -1:
                fa[y] = x
                depth[y] = depth[x] + 1
                stk.append(y)
    fa[a] = -1
    # print(dfs)

    size = [0] * n
    for x in dfs[::-1]:
        size[x] += 1
        if fa[x] >= 0:
            size[fa[x]] += size[x]

    ans = 2 * (size[a] - 1) - max(depth) + depth[b]
    print(ans)
