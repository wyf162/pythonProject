# -*- coding : utf-8 -*-
# @Time: 2023/10/4 13:48
# @Author: yefei.wang
# @File: P2052.py

import sys
from collections import Counter

sys.stdin = open('./../input.txt', 'r')
sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
edges = [LI() for _ in range(n - 1)]

g = [[] for i in range(n + 1)]
hst = Counter()
for u, v, w in edges:
    g[u].append(v)
    g[v].append(u)
    if u > v:
        u, v = v, u
    hst[(u, v)] = w

ans = 0


def dfs(x, fa):
    size = 1
    for y in g[x]:
        if y != fa:
            size_y = dfs(y, x)
            size += size_y
            u, v = x, y
            if u > v:
                u, v = v, u
            global ans
            ans += abs(size_y * 2 - n) * hst[(u, v)]
    return size


dfs(1, 0)

print(ans)
