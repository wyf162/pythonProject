# -*- coding : utf-8 -*-
# @Time: 2024/5/16 21:07
# @Author: yefei.wang
# @File: 1219G.py


import sys

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

tcn = 2
for _tcn_ in range(tcn):
    n, m = MI()
    mtx = [LI() for _ in range(n)]
    if n <= 4 or m <= 4:
        print(sum(sum(row) for row in mtx))
        continue
    if n > m:
        mtx = [[mtx[i][j] for i in range(n)] for j in range(m)]
        n, m = m, n
        # print(mtx)

    row = [0] * n
    col = [0] * m
    for i in range(n):
        for j in range(m):
            row[i] += mtx[i][j]
            col[j] += mtx[i][j]

    for i in range(n):
        tot = row[i]
        for j in range(m):
            col[j] -= mtx[i][j]
