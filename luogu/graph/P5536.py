# -*- coding : utf-8 -*-
# @Time: 2023/10/3 22:12
# @Author: yefei.wang
# @File: P5536.py


import sys
from collections import deque

sys.stdin = open('./../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, k = MI()
edges = [LI() for _ in range(n - 1)]

g = [[] for i in range(n + 1)]
deg = [0] * (n + 1)
for u, v in edges:
    g[u].append(v)
    g[v].append(u)
    deg[u] += 1
    deg[v] += 1

q = deque(i for i, d in enumerate(deg) if d == 1)

vis = set()
ans = 0
while True:
    for _ in range(len(q)):
        x = q.popleft()
        vis.add(x)
        for y in g[x]:
            deg[y] -= 1
            if y not in vis and deg[y] == 1:
                q.append(y)
    ans += 1
    if n - len(vis) <= k:
        break

print(ans)

