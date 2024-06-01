# -*- coding : utf-8 -*-
# @Time: 2024/6/1 21:18
# @Author: yefei.wang
# @File: 802J.py
# trees

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

n = I()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = MI()
    g[u].append((v, w))
    g[v].append((u, w))

father = [-1] * n
stk = [(0, -1)]
dfs = []
while stk:
    x, fa = stk.pop()
    dfs.append(x)
    for y, w in g[x]:
        if y != fa:
            stk.append((y, x))
            father[y] = x

dp = [0] * n
for x in dfs[::-1]:
    for y, w in g[x]:
        if y != father[x]:
            dp[x] = max(dp[x], dp[y] + w)
ans = max(dp)
print(ans)
