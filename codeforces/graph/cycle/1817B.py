# -*- coding: utf-8 -*-
# @Time: 2024/4/30 11:27
# @Author: yfwang
# @File: 1817B.py

import sys

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

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    edges = []
    for u in range(n):
        if edges: break
  
        ne_u = set(g[u])
        available = len(ne_u)
        stk = [u]
        path = []
        vis = [0] * n

        while stk:
            c = stk[-1]
            if not vis[c]:
                vis[c] = 1
                path.append(c)
                if c in ne_u:
                    available -= 1

                for ne in g[c]:
                    stk.append(ne)
            else:
                if c == u and len(path) >= 3:
                    if available >= 2:
                        path.append(u)
                        for i in range(len(path)-1):
                            edges.append((path[i], path[i+1]))
                        in_cycle = set(path)
                        used = 0
                        for ne in g[u]:
                            if ne not in in_cycle:
                                edges.append((ne, u))
                                used += 1
                            if used == 2:
                                break
                        break
                if path and path[-1] == c:
                    if c in ne_u:
                        available += 1
                    path.pop()
                stk.pop()
    if edges:
        print('YES')
        print(len(edges))
        for i in range(len(edges)):
            print(edges[i][0]+1, edges[i][1] + 1)
    else:
        print('NO')


































