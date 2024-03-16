# -*- coding : utf-8 -*-
# @Time: 2024/3/15 22:51
# @Author: yefei.wang
# @File: C.py

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    grid = [input() for _ in range(2)]
    q = deque()
    q.append((0, 0))
    vis = [[False] * n for _ in range(2)]
    vis[0][0] = True
    dp = [[False] * n for _ in range(2)]
    dp[0][0] = True
    ans = False
    while q:
        i, j = q.popleft()
        if j - 1 >= 0:
            if grid[i][j - 1] == '<':
                if j - 2 < 0:
                    continue
                dp[i][j - 2] = True
                if not vis[i][j - 2]:
                    q.append((i, j - 2))
                    vis[i][j - 2] = True
        if j + 1 < n:
            if grid[i][j + 1] == '>':
                if j + 2 >= n:
                    continue
                dp[i][j + 2] = True
                if not vis[i][j + 2]:
                    q.append((i, j + 2))
                    vis[i][j + 2] = True

        if grid[i ^ 1][j] == '>':
            if j + 1 >= n:
                continue
            dp[i ^ 1][j + 1] = True
            if not vis[i ^ 1][j + 1]:
                q.append((i ^ 1, j + 1))
                vis[i ^ 1][j + 1] = True

        if grid[i ^ 1][j] == '<':
            if j - 1 < 0:
                continue
            dp[i ^ 1][j - 1] = True
            if not vis[i ^ 1][j - 1]:
                q.append((i ^ 1, j - 1))
                vis[i ^ 1][j - 1] = True

    YN(dp[1][-1])
