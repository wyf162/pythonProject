# -*- coding : utf-8 -*-
# @Time: 2024/6/12 1:01
# @Author: yefei.wang
# @File: D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    grid = [list(input()) for _ in range(n)]
    row = [0] * n
    col = [0] * m
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                row[i] += 1
                col[j] += 1
    mx = max(row)
    i1 = row.index(mx)
    j1 = col.index(mx)
    print(i1+1, j1+1)
