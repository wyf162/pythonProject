# -*- coding : utf-8 -*-
# @Time: 2023/10/4 0:08
# @Author: yefei.wang
# @File: P3379-lca-01.py

import sys
sys.stdin = open('./../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, qs, root = MI()
edges = [LI() for _ in range(n - 1)]
queries = [LI() for _ in range(qs)]

g = [[] for i in range(n + 1)]
for u, v in edges:
    g[u].append(v)
    g[v].append(u)

depth = [0] * (n + 1)
father = [0] * (n + 1)


def dfs(x, fa, dep):
    depth[x] = dep
    father[x] = fa
    for y in g[x]:
        if y != fa:
            dfs(y, x, dep + 1)


dfs(root, 0, 1)

for a, b in queries:
    while depth[a] > depth[b]:
        a = father[a]
    while depth[b] > depth[a]:
        b = father[b]

    while a != b:
        a = father[a]
        b = father[b]
    print(a)
