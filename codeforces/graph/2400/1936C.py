# -*- coding: utf-8 -*-
# @Time: 2024/5/27 13:41
# @Author: yfwang
# @File: 1936C.py
# https://codeforces.com/problemset/problem/1936/C
# shortest paths sorting DP

import sys
from heapq import heappop, heappush

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
inf = 10 ** 18

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    cost = LI()
    attr = [LI() for i in range(n)]

    g = [[] for _ in range(n * (m + 1))]
    for i in range(n):
        for j in range(m):
            atti = (j + 1) * n + i
            g[i].append((atti, cost[i]))
            g[atti].append((i, 0))

    idx = list(range(n))
    for j in range(m):
        idx.sort(key=lambda x: attr[x][j])
        for i in range(1, n):
            x = (j + 1) * n + idx[i - 1]
            y = (j + 1) * n + idx[i]
            g[x].append((y, attr[idx[i]][j] - attr[idx[i - 1]][j]))
            g[y].append((x, 0))

    dist = [inf] * (n * (m + 1))
    dist[n-1] = 0
    h = [(0, n-1)]
    while h:
        d, x = heappop(h)
        if d > dist[x]:
            continue
        for y, w in g[x]:
            if d + w < dist[y]:
                dist[y] = d + w
                heappush(h, (dist[y], y))
    print(dist[0])















