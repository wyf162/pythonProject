# -*- coding : utf-8 -*-
# @Time: 2023/10/1 16:22
# @Author: yefei.wang
# @File: 1873H2.py

import sys
from collections import deque

# sys.stdin = open('./../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, a, b = MI()
    edges = [LI() for i in range(n)]
    a -= 1
    b -= 1
    if a == b:
        print('NO')
        continue

    g = [[] for _ in range(n)]
    deg = [0] * n
    for u, v in edges:
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    vis = [False] * n
    q = deque(i for i, d in enumerate(deg) if d == 1)
    while q:
        x = q.popleft()
        vis[x] = True
        for y in g[x]:
            deg[y] -= 1
            if deg[y] == 1 and not vis[y]:
                q.append(y)

    depth = [0] * n
    father = [_ for _ in range(n)]


    def dfs(x, fa, dep):
        depth[x] = dep
        father[x] = father[fa]
        for y in g[x]:

            if y != fa and deg[y] != 2:
                dfs(y, x, dep + 1)


    for i in range(n):
        if deg[i] == 2 and len(g[i]) > 2:
            dfs(i, i, 0)


    def dist(s, fa, t):
        if s == t:
            return 0
        d = n
        for e in g[s]:
            if deg[e] == 2 and e != fa:
                d = min(d, 1 + dist(e, s, t))
        return d


    if father[a] == father[b] and depth[a] <= depth[b]:
        print('NO')
        continue
    elif not (deg[a] == 2 and deg[b] == 2):
        x, y = father[a], father[b]
        dxy = dist(x, -1, y)
        if dxy + depth[a] <= depth[b]:
            print('NO')
            continue
    print('YES')
