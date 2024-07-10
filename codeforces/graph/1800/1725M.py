# -*- coding: utf-8 -*-
# @Time: 2024/7/10 9:23
# @Author: yfwang
# @File: 1725M.py
# Dijkstra

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
inf = 10 ** 15

n, m = MI()
g = [[] for _ in range(n * 2)]
for x in range(n):
    g[x].append((x + n, 0))

for _ in range(m):
    u, v, w = GMI()
    g[u].append((v, w + 1))
    g[n + v].append((n + u, w + 1))

dis = [inf] * (2 * n)
dis[0] = 0
h = []
mask = (1 << 20) - 1
heappush(h, 0)
while h:
    s = heappop(h)
    d, x = s >> 20, s & mask
    if d > dis[x]:
        continue
    for y, w in g[x]:
        if d + w < dis[y]:
            dis[y] = d + w
            heappush(h, dis[y] << 20 | y)

rets = [0] * n
for i in range(1, n):
    rets[i] = min(dis[i], dis[i + n])
    if rets[i] >= inf:
        rets[i] = -1
print(*rets[1:])
