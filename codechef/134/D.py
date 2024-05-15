# -*- coding : utf-8 -*-
# @Time: 2024/5/15 23:48
# @Author: yefei.wang
# @File: D.py

import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 0x3f3f3f3f

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    mtx = [list(int(x) for x in input()) for _ in range(n)]
    h = []
    vis = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        heappush(h, (mtx[i][0], i, 0))
        heappush(h, (mtx[i][m - 1], i, m - 1))
        vis[i][0] = mtx[i][0]
        vis[i][m - 1] = mtx[i][m - 1]

    for j in range(m):
        heappush(h, (mtx[0][j], 0, j))
        heappush(h, (mtx[n - 1][j], n - 1, j))
        vis[0][j] = mtx[0][j]
        vis[n - 1][j] = mtx[n - 1][j]

    while h:
        d, x, y = heappop(h)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if vis[nx][ny] == -1:
                    heappush(h, (mtx[nx][ny] + d, nx, ny))
                    vis[nx][ny] = mtx[nx][ny] + d

    for i in range(n):
        for j in range(m):
            if mtx[i][j] == 1:
                vis[i][j] = 0
    ans = max(max(vis[i]) for i in range(n))
    print(ans)

    # dp = [[inf for _ in range(m)] for _ in range(n)]
    # for i in range(n):
    #     dp[i][0] = mtx[i][0]
    #     dp[i][m - 1] = mtx[i][m - 1]
    # for j in range(m):
    #     dp[0][j] = mtx[0][j]
    #     dp[n - 1][j] = mtx[n - 1][j]
    #
    # for k in range(1, n // 2 + 1):
    #     for i in range(k, n - k):
    #         dp[i][k] = min(dp[i][k], dp[i][k - 1] + mtx[i][k], dp[i - 1][k] + mtx[i][k])
    #         dp[i][m - k - 1] = min(dp[i][m - k - 1], dp[i][m - k] + mtx[i][k], dp[i - 1][m - k] + mtx[i][k])
    #
    #     # for j in range(k, m - k):
    #     #     dp[k][j] = min(dp[k][j], dp[k][j-1] + mtx[k][j], dp[k-1][j] + mtx[k][j])
    #     #     dp[m-k][j] = min(dp[m-k][j], dp[m-k][j-1]+mtx[k][j], dp[m-k+1][j]+mtx[k][j])
    # for i in range(n):
    #     for j in range(m):
    #         if mtx[i][j] == 1:
    #             dp[i][j] = 0
    # ans = max(max(dp[i]) for i in range(n))
    # print(ans)
