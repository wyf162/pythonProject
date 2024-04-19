# -*- coding: utf-8 -*-
# @Time: 2024/4/19 11:27
# @Author: yfwang
# @File: demo_dfs.py

#  dfs 求树的直径
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
g = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)

vis = [0] * n
vis[0] = 1
dq = deque([0])
while dq:
    u = dq.popleft()
    for v in g[u]:
        if not vis[v]:
            vis[v] = 1
            dq.append(v)

v1 = u
parent = [-1] * n
dis1 = [0] * n
vis[v1] = 0
dq = deque([v1])
while dq:
    u = dq.popleft()
    for v in g[u]:
        if vis[v]:
            vis[v] = 0
            dq.append(v)
            parent[v] = u
            dis1[v] = dis1[u] + 1
v2 = u

dis2 = [-1] * n
dis2[v2] = 0
stack = [v2]
while stack:
    u = stack.pop()
    for v in g[u]:
        if dis2[v] == -1:
            stack.append(v)
            dis2[v] = dis2[u] + 1

diameter = [v2]
in_diameter = [0] * n
in_diameter[v2] = 1
while diameter[-1] != v1:
    diameter.append(parent[diameter[-1]])
    in_diameter[diameter[-1]] = 1

