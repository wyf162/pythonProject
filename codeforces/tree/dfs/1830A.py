# -*- coding : utf-8 -*-
# @Time: 2024/2/3 17:01
# @Author: yefei.wang
# @File: 1830A.py

import sys
from collections import Counter

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
    edges = [LGMI() for _ in range(n - 1)]
    g = [[] for _ in range(n)]
    hst = Counter()
    idx = 1
    for u, v in edges:
        g[v].append(u)
        g[u].append(v)
        if v > u: u, v = v, u
        hst[(v, u)] = idx
        idx += 1

    fa = [-1] * n
    tree = [[] for _ in range(n)]
    fa[0] = n
    q = [0]
    while q:
        x = q.pop()
        for y in g[x]:
            if fa[y] == -1:
                fa[y] = x
                tree[x].append(y)
                q.append(y)

    dp = [0] * n
    stk = [0]
    dp[0] = 1
    while stk:
        x = stk.pop()
        for y in tree[x]:
            x1, y1 = fa[x], x
            if x1 > y1: x1, y1 = y1, x1
            e1 = (x1, y1)
            x2, y2 = x, y
            if x2 > y2: x2, y2 = y2, x2
            e2 = (x2, y2)
            if hst[e1] < hst[e2]:
                dp[y] = dp[x]
            else:
                dp[y] = dp[x] + 1
            stk.append(y)
    print(max(dp))
