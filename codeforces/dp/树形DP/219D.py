# -*- coding : utf-8 -*-
# @Time: 2024/1/31 21:12
# @Author: yefei.wang
# @File: 219D.py

import sys

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
    g[u].append((v, 0))
    g[v].append((u, 1))

stk = [(0, -1)]
dp = [0] * n
while stk:
    x, fa = stk.pop()
    for y, w in g[x]:
        if y != fa:
            dp[0] += w
            stk.append((y, x))
# print(dp)

stk = [(0, -1)]
while stk:
    x, fa = stk.pop()
    for y, w in g[x]:
        if y != fa:
            dp[y] = dp[x] + (1 if w == 0 else -1)
            stk.append((y, x))
mi = min(dp)
print(mi)
print(*[i + 1 for i, x in enumerate(dp) if x == mi])
