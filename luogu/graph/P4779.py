# -*- coding : utf-8 -*-
# @Time: 2024/6/19 21:33
# @Author: yefei.wang
# @File: P4779.py

import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
inf = 10 ** 9

n, m, s = MI()
s -= 1
g = [[] for _ in range(n)]
for i in range(m):
    u, v, w = MI()
    u -= 1
    v -= 1
    g[u].append((v, w))

dis = [inf for _ in range(n)]
dis[0] = 0
h = []
heappush(h, (0, 0))
while h:
    d, x = heappop(h)
    if d > dis[x]:
        continue
    for y, w in g[x]:
        if d + w < dis[y]:
            dis[y] = d + w
            heappush(h, (dis[y], y))
print(*dis)
