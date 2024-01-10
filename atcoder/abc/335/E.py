# -*- coding : utf-8 -*-
# @Time: 2024/1/6 20:40
# @Author: yefei.wang
# @File: E.py

import sys
from collections import deque
from heapq import heappop, heappush

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

n, m = MI()
A = LI()
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)

dep = [0] * n
vis = [0] * n
h = []
heappush(h, [A[0], 0])
vis[0] = 1
dep[0] = 1
while h:
    v, x = heappop(h)
    for y in g[x]:
        if A[y] > A[x]:
            dep[y] = max(dep[y], dep[x] + 1)
            if not vis[y]:
                heappush(h, [A[y], y])
                vis[y] = 1
        elif A[y] == A[x]:
            dep[y] = max(dep[y], dep[x])
            if not vis[y]:
                heappush(h, [A[y], y])
                vis[y] = 1
print(dep[-1])
