# -*- coding : utf-8 -*-
# @Time: 2023/10/3 13:02
# @Author: yefei.wang
# @File: P1064.py

import sys

sys.stdin = open('./../../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
n //= 10

ll = [LI() for _ in range(m)]

# price, multi, father
price, multi, father = [], [], []
for i in range(m):
    p, mu, fa = ll[i]
    p //= 10
    price.append(p)
    multi.append(mu)
    father.append(fa)
price.insert(0, None)
multi.insert(0, None)
father.insert(0, None)

g = [[] for i in range(m + 1)]
for i, fa in enumerate(father[1:], start=1):
    if fa != 0:
        g[fa].append(i)
    else:
        g[0].append(i)

# print(g)

dp = [[0 for j in range(n + 1)] for i in range(m + 1)]


def dfs(u, t):
    if t <= 0:
        return

    for v in g[u]:
        for k in range(t - price[i], - 1, -1):
            dp[v][k] = dp[u][k] + price[v] * multi[v]

        dfs(v, t - price[v])
        for k in range(n, price[v] - 1, -1):
            dp[u][k] = max(dp[u][k], dp[v][k - price[v]])


dfs(0, n)

rst = max(dp[0])
print(rst * 10)
