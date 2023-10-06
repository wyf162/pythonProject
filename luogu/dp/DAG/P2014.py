# -*- coding : utf-8 -*-
# @Time: 2023/10/3 15:03
# @Author: yefei.wang
# @File: P2014.py
from collections import deque
import sys

sys.stdin = open('./../../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
courses = [LI() for _ in range(n)]
scores = [0] * (n + 1)
g = [[] for _ in range(n + 1)]

for i, ks in enumerate(courses):
    pre, score = ks
    scores[i + 1] = score
    if pre:
        g[pre].append(i + 1)
    else:
        g[0].append(i+1)
# print(scores)
# print(g)

dp = [[0 for j in range(m + 1)] for i in range(n + 1)]


def dfs(u, t):
    if t <= 0:
        return
    for v in g[u]:
        for k in range(t):
            dp[v][k] = dp[u][k] + scores[v]
        dfs(v, t - 1)
        for k in range(1, t + 1):
            dp[u][k] = max(dp[u][k], dp[v][k - 1])


dfs(0, m)

print(dp[0][m])
