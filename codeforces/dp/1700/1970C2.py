# -*- coding: utf-8 -*-
# @Time: 2024/7/8 17:20
# @Author: yfwang
# @File: 1970C1.py
# game

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, t = MI()

g = [[] for _ in range(n)]
deg = [0 for _ in range(n)]
for _ in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)
    deg[u] += 1
    deg[v] += 1

queries = LGMI()
root = queries[0]

parent = [-1] * n
depth = [0] * n
stk = [root]
dfs = []
while stk:
    x = stk.pop()
    dfs.append(x)
    for y in g[x]:
        if parent[x] != y:
            parent[y] = x
            depth[y] = depth[x] + 1
            stk.append(y)

# print(depth)
# print(dfs)
ans = [False for _ in range(n)]
for x in dfs[::-1]:
    fa = parent[x]
    if fa >= 0:
        ans[fa] |= not ans[x]

print('Ron' if ans[root] else 'Hermione')

