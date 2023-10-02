# -*- coding : utf-8 -*-
# @Time: 2023/10/2 14:20
# @Author: yefei.wang
# @File: c.py


import sys

sys.stdin = open('./../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, k = MI()
a = LI()
b = LI()

colors = list(sorted(list(set(a))))
m = len(colors)
c2v = {c: i for i, c in enumerate(colors)}

mtx = [[True for j in range(m)] for i in range(m)]

for i in range(n):
    for j in range(i + 1, n):
        if a[j] < a[i]:
            u, v = c2v[a[j]], c2v[a[i]]
            mtx[u][v] = False
            mtx[v][u] = False

g = [[] for _ in range(m)]
for i in range(m):
    for j in range(m):
        if mtx[i][j]:
            g[i].append(j)

N = m
dfn = [0] * N
low = [0] * N
dfncnt = 0
s = [0] * N
in_stack = [0] * N
tp = 0
scc = [0] * N
sc = 0  # 结点 i 所在 SCC 的编号
sz = [0] * N  # 强连通 i 的大小


def tarjan(u):
    global dfncnt, tp, sc
    low[u] = dfn[u] = dfncnt
    s[tp] = u
    in_stack[u] = 1
    dfncnt = dfncnt + 1
    tp = tp + 1
    for v in g[u]:
        if dfn[v] == False:
            tarjan(v)
            low[u] = min(low[u], low[v])
        elif in_stack[v]:
            low[u] = min(low[u], dfn[v])
    if dfn[u] == low[u]:
        sc = sc + 1
        while s[tp] != u:
            scc[s[tp]] = sc
            sz[sc] = sz[sc] + 1
            in_stack[s[tp]] = 0
            tp = tp - 1
        scc[s[tp]] = sc
        sz[sc] = sz[sc] + 1
        in_stack[s[tp]] = 0
        tp = tp - 1

tarjan(0)
print(scc)