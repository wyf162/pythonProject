# -*- coding : utf-8 -*-
# @Time: 2024/5/16 21:07
# @Author: yefei.wang
# @File: 1219G.py
# https://codeforces.com/problemset/problem/1219/G
# n^1.5

import sys
from heapq import nlargest

# sys.stdin = open('../../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip()
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 1
for _tcn_ in range(tcn):
    m, n = LI()
    grid = [LI() for _ in range(m)]
    if m > n:
        m, n = n, m
        grid = list(zip(*grid))
    rowsum = [sum(row) for row in grid]
    colsum = [sum(col) for col in zip(*grid)]

    ans = 0
    ans = max(ans, sum(nlargest(4, rowsum)))
    ans = max(ans, sum(nlargest(4, colsum)))

    for j, col in enumerate(zip(*grid)):
        for i, x in enumerate(col):
            rowsum[i] -= x
        ans = max(ans, colsum[j] + sum(nlargest(3, rowsum)))
        for i, x in enumerate(col):
            rowsum[i] += x
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            colsum[j] -= x
        ans = max(ans, rowsum[i] + sum(nlargest(3, colsum)))
        for j, x in enumerate(row):
            colsum[j] += x

    for i1 in range(m):
        for i2 in range(i1 + 1, m):
            for j in range(n):
                colsum[j] -= grid[i1][j] + grid[i2][j]
            ans = max(ans, rowsum[i1] + rowsum[i2] + sum(nlargest(2, colsum)))
            for j in range(n):
                colsum[j] += grid[i1][j] + grid[i2][j]

    print(ans)
