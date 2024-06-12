# -*- coding: utf-8 -*-
# @Time: 2024/6/12 14:09
# @Author: yfwang
# @File: 666B2.py

import sys
from collections import defaultdict

from heapq import heappop, heappush, nlargest

input = lambda: sys.stdin.readline().rstrip()
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

n, m = MI()
g = [[] for _ in range(n)]
for i in range(m):
    u, v = GMI()
    g[u].append(v)

f = lambda i, j: i * n + j

mtx = [-1 for _ in range(n * n)]

for i in range(n):
    mtx[f(i, i)] = 0
    h = [(0, i)]
    while h:
        d, x = heappop(h)
        for y in g[x]:
            if mtx[f(i, y)] == -1:
                mtx[f(i, y)] = d + 1
                heappush(h, (d + 1, y))

from_vertex = defaultdict(list)
to_vertex = defaultdict(list)
for i in range(n):
    for j in range(n):
        if mtx[f(i, j)] > 0:
            from_vertex[i].append(j)
            to_vertex[j].append(i)
for i in range(n):
    from_vertex[i] = nlargest(3, from_vertex[i], key=lambda x: mtx[f(i, x)])
for j in range(n):
    to_vertex[j] = nlargest(3, to_vertex[j], key=lambda x: mtx[f(x, j)])

ans = 0
path = None
for i in range(n):
    for j in range(n):
        if mtx[f(i, j)] <= 0:
            continue
        for h in to_vertex[i][:3]:
            for k in from_vertex[j][:3]:
                if h == k or k == i or h == j:
                    continue
                bns = mtx[f(h, i)] + mtx[f(i, j)] + mtx[f(j, k)]
                if bns > ans:
                    ans = bns
                    path = (h, i, j, k)

print(' '.join(str(x + 1) for x in path))
