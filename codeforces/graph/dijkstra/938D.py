# -*- coding: utf-8 -*-
# @Time: 2024/5/9 9:03
# @Author: yfwang
# @File: 938D.py
# https://codeforces.com/problemset/problem/938/D

import sys
from heapq import heapify, heappush, heappop

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

tcn = 2
for _tcn_ in range(tcn):
    n, m = MI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = MI()
        u -= 1
        v -= 1
        g[u].append((v, 2*w))
        g[v].append((u, 2*w))
    dist = LI()
    h = [(dist[i], i) for i in range(n)]
    heapify(h)
    while h:
        d, x = heappop(h)
        if d > dist[x]:
            continue
        for y, w in g[x]:
            if d + w < dist[y]:
                dist[y] = d + w
                heappush(h, (dist[y], y))
    print(*dist)




































