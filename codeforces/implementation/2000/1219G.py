# -*- coding : utf-8 -*-
# @Time: 2024/5/16 21:07
# @Author: yefei.wang
# @File: 1219G.py
# https://codeforces.com/problemset/problem/1219/G
# n^1.5

import sys
from heapq import heappop, heapify

sys.stdin = open('../../input.txt', 'r')
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
    n, m = MI()
    mtx = [LI() for _ in range(n)]
    if n <= 4 or m <= 4:
        print(sum(sum(row) for row in mtx))
        continue

    row = [0] * n
    col = [0] * m
    for i in range(n):
        for j in range(m):
            row[i] += mtx[i][j]
            col[j] += mtx[i][j]

    ans = 0
    for i in range(n):
        h = [-col[j] + mtx[i][j] for j in range(m)]
        heapify(h)
        ans = max(ans, row[i] - heappop(h) - heappop(h) - heappop(h))

    for j in range(m):
        h = [-row[i] + mtx[i][j] for i in range(n)]
        heapify(h)
        ans = max(ans, col[j] - heappop(h) - heappop(h) - heappop(h))

    if n <= m:
        for i1 in range(n):
            for i2 in range(i1 + 1, n):
                h = [-col[j] + mtx[i1][j] + mtx[i2][j] for j in range(m)]
                heapify(h)
                ans = max(ans, row[i1] + row[i2] - heappop(h) - heappop(h))
    else:
        for j1 in range(m):
            for j2 in range(j1 + 1, m):
                h = [-row[i] + mtx[i][j1] + mtx[i][j1] for i in range(n)]
                heapify(h)
                ans = max(ans, row[j1] + row[j2] - heappop(h) - heappop(h))

    h = [-row[i] for i in range(n)]
    heapify(h)
    ans = max(ans, -heappop(h) - heappop(h) - heappop(h) - heappop(h))

    h = [-col[j] for j in range(m)]
    heapify(h)
    ans = max(ans, -heappop(h) - heappop(h) - heappop(h) - heappop(h))
    print(ans)
