# -*- coding: utf-8 -*-
# @Time: 2024/7/5 14:39
# @Author: yfwang
# @File: 1927F.py

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 10 ** 9


def find_SCC(graph, n):
    SCC, S, P = [], [], []
    depth = [0] * n

    stack = list(range(n))
    while stack:
        node = stack.pop()
        if node < 0:
            d = depth[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:], P[-1]
                for node in SCC[-1]:
                    depth[node] = -1
        elif depth[node] > 0:
            while P[-1] > depth[node]:
                P.pop()
        elif depth[node] == 0:
            S.append(node)
            P.append(len(S))
            depth[node] = len(S)
            stack.append(~node)
            stack += graph[node]
    return SCC[::-1]


tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    g = [[] for _ in range(n)]
    hst = dict()
    for _ in range(m):
        u, v, w = GMI()
        hst[(u, v)] = w + 1
        hst[(v, u)] = w + 1
        g[u].append(v)
        g[v].append(u)

    scc = find_SCC(g, n)
    cost = [inf for _ in range(len(scc))]
    for i, sc in enumerate(scc):
        st = set(sc)
        for x in sc:
            for y in g[x]:
                if y in st:
                    cost[i] = min(cost[i], hst[(x, y)])
    mi = min(cost)
    i = cost.index(mi)
    sc = scc[i]
    st = set(sc)
    e1, e2 = None, None
    for x in sc:
        for y in g[x]:
            if y in st:
                if hst[(x, y)] == mi:
                    e1, e2 = x, y
                    break
        if e1 is not None:
            break

    # print(e1, '->', e2)
    q1 = deque()
    q1.append(e1)
    par1 = dict()
    vis1 = {e1}
    while q1:
        x = q1.popleft()
        for y in g[x]:
            if y == e2:
                continue
            if y not in vis1:
                par1[y] = x
                q1.append(y)
                vis1.add(y)

    q2 = deque()
    q2.append(e2)
    par2 = dict()
    vis2 = {e2}
    while q2:
        x = q2.popleft()
        if x in vis1:
            path1 = []
            cur = x
            while cur != e1:
                path1.append(cur)
                cur = par1[cur]
            path1.append(e1)
            path2 = []
            cur = x
            while cur != e2:
                path2.append(cur)
                cur = par2[cur]
            path2.append(e2)
            path = path1[1:] + path2[::-1]
            break
        for y in g[x]:
            if y == e1:
                continue
            if y not in vis2:
                par2[y] = x
                q2.append(y)
                vis2.add(y)

    print(mi, len(path))
    print(' '.join(str(x + 1) for x in path))
