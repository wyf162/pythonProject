# -*- coding: utf-8 -*-
# @Time: 2024/4/10 11:23
# @Author: yfwang
# @File: 1102F.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, m = MI()
grid = [LI() for _ in range(n)]

inf = 10 ** 9
conse_diff = [[inf] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != j:
            conse_diff[i][j] = min(abs(grid[i][idx] - grid[j][idx]) for idx in range(m))


def p(msk, i, j):
    return (msk * n + i) * n + j


dp = [0] * (n * n << n)
for i in range(n):
    dp[p(1 << i, i, i)] = inf

for msk in range(1 << n):
    for i in range(n):
        for j in range(n):
            if dp[p(msk, i, j)]:
                old = dp[p(msk, i, j)]
                for nj in range(n):
                    if msk >> nj & 1 == 0:
                        new_status = p(msk | (1 << nj), i, nj)
                        dp[new_status] = max(dp[new_status], min(old, conse_diff[j][nj]))

ans = 0
for i in range(n):
    for j in range(n):
        cur = dp[p((1 << n) - 1, i, j)]
        for idx in range(m - 1):
            cur = min(cur, abs(grid[j][idx] - grid[i][idx + 1]))
        ans = max(ans, cur)

print(ans)
