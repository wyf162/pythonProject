# -*- coding: utf-8 -*-
# @Time: 2024/5/28 16:49
# @Author: yfwang
# @File: 1083A.py
# https://codeforces.com/contest/1083/problem/A
# trees DP

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
nums = LI()

g = [[] for _ in range(n)]
for i in range(n - 1):
    u, v, w = GMI()
    w += 1
    g[u].append((v, w))
    g[v].append((u, w))

ans = 0

fa = [-1] * n
dfs = []
stk = [0]
fa[0] = n

while stk:
    x = stk.pop()
    dfs.append(x)
    for y, w in g[x]:
        if fa[y] == -1:
            fa[y] = x
            stk.append(y)
fa[0] = -1

dp = [0] * n
for x in dfs[::-1]:
    dp[x] = nums[x]
    rets = []
    for y, w in g[x]:
        if y == fa[x]:
            continue
        rets.append(dp[y] - w + nums[x])

    rets.sort(reverse=True)
    if len(rets) == 0:
        ans = max(nums[x], ans)
    if len(rets) >= 1:
        ans = max(rets[0], ans)
    if len(rets) >= 2:
        ans = max(ans, rets[0] + rets[1] - nums[x])

    if rets:
        dp[x] = max(rets[0], nums[x])
    else:
        dp[x] = nums[x]

print(ans)
