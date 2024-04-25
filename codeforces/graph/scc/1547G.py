# -*- coding: utf-8 -*-
# @Time: 2024/4/24 17:28
# @Author: yfwang
# @File: 1547G.py
# https://codeforces.com/contest/1547/problem/G
# 强连通分量

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
INF = 0x3f3f3f3f


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
    input()
    n, m = MI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = GMI()
        g[u].append(v)

    ans = [0] * n
    ans[0] = 1
    stack = [0]
    while stack:
        u = stack.pop()
        for v in g[u]:
            if ans[v] < 2:
                ans[v] += 1
                stack.append(v)
    stack = []
    scc = find_SCC(g, n)
    for i in range(len(scc)):
        if len(scc[i]) > 1 and ans[scc[i][0]] > 0:
            for x in scc[i]:
                stack.append(x)
                ans[x] = -1

    for i in range(n):
        if i in g[i] and ans[i] > 0:
            ans[i] = -1
            stack.append(i)

    while stack:
        u = stack.pop()
        for v in g[u]:
            if ans[v] != -1:
                ans[v] = -1
                stack.append(v)
    print(*ans)
