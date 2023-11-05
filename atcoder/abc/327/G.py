# -*- coding : utf-8 -*-
# @Time: 2023/11/4 21:00
# @Author: yefei.wang
# @File: G.py

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

N, M = MI()
A = LI()
B = LI()
mod = 10 ** 9 + 7
g = [set() for _ in range(N)]

for x, y in zip(A, B):
    if x == y:
        exit(print('No'))
    x -= 1
    y -= 1
    g[x].add(y)
    g[y].add(x)

group = [0] * N
tag = 0
ans = 1
for i in range(N):
    if group[i] == 0:
        tag += 1
        group[i] = tag
        dp = [[0, 0] for _ in range(N)]

        stk = [[i, -1]]
        sstk = []
        while stk:
            x, fa = stk.pop()
            dp[x][0] = dp[x][1] = 1
            for y in g[x]:
                group[y] = tag
                if y == fa:
                    continue
                stk.append([y, x])
                sstk.append([y, x])

        while sstk:
            y, x = sstk.pop()
            dp[x][1] = dp[x][1] * dp[y][0] % mod
            dp[x][0] = dp[x][0] * (dp[y][0] + dp[y][1]) % mod

        rst = sum(dp[0]) % mod
        ans *= rst
        ans %= mod
print(ans)
