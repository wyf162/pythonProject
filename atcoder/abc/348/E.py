# -*- coding : utf-8 -*-
# @Time: 2024/4/6 21:13
# @Author: yefei.wang
# @File: E.py

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
Yn = lambda x: print('Yes' if x else 'No')
mod = 1000000007
mod2 = 998244353

n = I()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)
cost = LI()

fa = [-1] * n
dfs = []
stk = [0]
fa[0] = n
depth = [0] * n

while stk:
    x = stk.pop()
    dfs.append(x)
    for y in g[x]:
        if fa[y] == -1:
            fa[y] = x
            depth[y] = depth[x] + 1
            stk.append(y)
fa[0] = -1
# print(depth)

size = [0] * n
for x in dfs[::-1]:
    size[x] += cost[x]
    if fa[x] >= 0:
        size[fa[x]] += size[x]
# print(size)

dp = [0] * n
for i in range(1, n):
    dp[0] += cost[i] * depth[i]
# print(dp)

tot = sum(cost)
for y in dfs[1:]:
    x = fa[y]
    dp[y] = dp[x] - (size[y] - cost[y]) + tot - size[y] - cost[y]
# print(dp)
print(min(dp))
