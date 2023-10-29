# -*- coding : utf-8 -*-
# @Time: 2023/10/24 20:42
# @Author: yefei.wang
# @File: d.py

import os
import sys
from heapq import heappop, heappush

# 请在此输入您的代码
sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, p = MI()
g = [[] for i in range(n)]
s = [0] * n
k = [0] * n
deg = [0] * n
for i in range(n):
    f, si, ki = MI()
    s[i], k[i] = si, ki
    f -= 1
    if f >= 0:
        g[f].append(i)
        deg[i] += 1


pq = []
for i in range(n):
    if deg[i] == 0:
        heappush(pq, (k[i], i))

ans = 0
while pq:
    if pq[0][0] <= p:
        ans += 1
        p += s[pq[0][1]]
        _, x = heappop(pq)
        for y in g[x]:
            deg[y] -= 1
            if deg[y] == 0:
                heappush(pq, (k[y], y))
    else:
        break

print(ans)
