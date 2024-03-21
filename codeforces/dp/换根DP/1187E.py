# -*- coding: utf-8 -*-
# @Time: 2024/3/21 9:06
# @Author: yfwang
# @File: 1187E.py
# https://codeforces.com/problemset/problem/1187/E

import sys
from collections import deque

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

n = I()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)

fa = [-1] * n
dfs = []
stk = [0]
fa[0] = n
while stk:
    x = stk.pop()
    dfs.append(x)
    for y in g[x]:
        if fa[y] == -1:
            fa[y] = x
            stk.append(y)

sz = [0] * n
for x in dfs[::-1]:
    sz[x] += 1
    if fa[x] < n:
        sz[fa[x]] += sz[x]

# print(sz)
dp = [0] * n
for x in dfs[::-1]:
    dp[0] += sz[x]
# print(dp[0])

for x in dfs[1:]:
    y = fa[x]
    dp[x] = dp[y] - sz[x] + n - sz[x]

print(max(dp))
