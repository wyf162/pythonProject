# -*- coding: utf-8 -*-
# @Time: 2024/6/26 14:29
# @Author: yfwang
# @File: 1970C.py

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

import sys

n, t = MI()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)
deg = [len(vv) for vv in g]
q = deque(u for u, d in enumerate(deg) if d == 1)
dfs = []

pos = [-1] * n
p = 0
while q:
    x = q.popleft()
    dfs.append(x)
    pos[x] = p
    p += 1
    for y in g[x]:
        deg[y] -= 1
        if deg[y] == 1:
            q.append(y)


ans = [0] * n
for x in dfs:
    for y in g[x]:
        if pos[y] < pos[x]:
            ans[x] += not ans[y]

for x in dfs[::-1]:
    for y in g[x]:
        if pos[y] > pos[x]:
            ans[x] += not (ans[y] - (not ans[x]))

uu = LGMI()

for u in uu:
    print("Ron" if ans[u] else "Hermione")
