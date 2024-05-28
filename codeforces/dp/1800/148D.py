# -*- coding: utf-8 -*-
# @Time: 2024/5/9 17:40
# @Author: yfwang
# @File: 148D.py
# https://codeforces.com/problemset/problem/148/D
# probabilities

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
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
    w, b = map(int, input().split())

    fP = [[0] * (b + 1) for i in range(w + 1)]
    fD = [[0] * (b + 1) for i in range(w + 1)]
    for i in range(w + 1):
        for j in range(b + 1):
            if i + j == 0:
                fP[i][j] = 0
                fD[i][j] = 1
            elif j == 0:
                fP[i][j] = fD[i][j] = 1
            else:
                fP[i][j] = i / (i + j) + j / (i + j) * (1 - fD[i][j - 1])
                fD[i][j] = i / (i + j) + j / (i + j) * (
                    (1 - fP[i - 1][j - 1]) if j == 1 else (j - 1) / (i + j - 1) * (1 - fP[i][j - 2]) + i / (
                            i + j - 1) * (1 - fP[i - 1][j - 1]))
    print(fP[w][b])

