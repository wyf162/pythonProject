# -*- coding : utf-8 -*-
# @Time: 2023/10/3 17:21
# @Author: yefei.wang
# @File: P4017.py


import sys
from collections import deque

sys.stdin = open('./../../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
edges = [LI() for _ in range(m)]
g = [[] for i in range(n + 1)]
deg = [0] * (n + 1)

for u, v in edges:
    g[u].append(v)
    deg[v] += 1

ends = []
for i, adj in enumerate(g):
    if len(adj) == 0:
        ends.append(i)

dp = [0] * (n + 1)
q = deque()
for i, d in enumerate(deg[1:], start=1):
    if d == 0:
        q.append(i)
        dp[i] = 1


while q:
    x = q.popleft()
    for y in g[x]:
        dp[y] += dp[x]
        deg[y] -= 1
        if deg[y] == 0:
            q.append(y)

mod = 80112002

rst = sum(dp[i] for i in ends)
rst %= mod
print(rst)
