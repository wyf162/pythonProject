# -*- coding : utf-8 -*-
# @Time: 2024/7/18 22:35
# @Author: yefei.wang
# @File: A.py

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
    A = [LI() for _ in range(n)]
    if n * m == 1:
        print(-1)
        continue
    B = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            k = i * m + j - 1
            if k < 0:
                k += n * m
            i1, i2 = k // m, k % m
            B[i1][i2] = A[i][j]
    for i in range(n):
        print(*B[i])
