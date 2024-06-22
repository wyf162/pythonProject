# -*- coding : utf-8 -*-
# @Time: 2024/6/22 14:31
# @Author: yefei.wang
# @File: 20C.py
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
inf = 10 ** 18

n, m = MI()
g = [[] for _ in range(n)]
for i in range(m):
    u, v, w = GMI()
    w += 1
    g[u].append([v, w])
    g[v].append([u, w])

dis = [inf for _ in range(n)]
par = [-1 for _ in range(n)]

dis[0] = 0
h = [(0, 0)]

while h:
    d, x = heappop(h)
    if dis[x] < d:
        continue
    for y, w in g[x]:
        if d + w < dis[y]:
            dis[y] = d + w
            par[y] = x
            heappush(h, (dis[y], y))

if dis[n-1] < inf:
    path = [n - 1]
    cur = n - 1
    while cur != 0:
        cur = par[cur]
        path.append(cur)
    print(' '.join(str(x+1) for x in path[::-1]))
else:
    print(-1)
