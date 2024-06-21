# -*- coding: utf-8 -*-
# @Time: 2024/6/21 13:32
# @Author: yfwang
# @File: 1957D.py
# bitmasks xor

import sys

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    f0 = [[0] * 31 for _ in range(n + 1)]
    f1 = [[0] * 31 for _ in range(n + 1)]
    # f0[0] = [1] * 31

    for i, a in enumerate(A):
        for j in range(31):
            if a >> j & 1:
                f1[i + 1][j] = f0[i][j] + 1
                f0[i + 1][j] = f1[i][j]
            else:
                f0[i + 1][j] = f0[i][j] + 1
                f1[i + 1][j] = f1[i][j]
        # print(f0[i+1])
        # print(f1[i+1])

    g0 = [[0] * 31 for _ in range(n + 1)]
    g1 = [[0] * 31 for _ in range(n + 1)]
    # g0[n] = [1] * 31

    for i in range(n - 1, -1, -1):
        a = A[i]
        for j in range(31):
            if a >> j & 1:
                g1[i][j] = g0[i + 1][j] + 1
                g0[i][j] = g1[i + 1][j]
            else:
                g0[i][j] = g0[i + 1][j] + 1
                g1[i][j] = g1[i + 1][j]
    ans = 0
    for i in range(n):
        x = A[i].bit_length() - 1
        c0 = (f0[i][x] + 1) * g0[i][x]
        c1 = f1[i][x] * g1[i][x]
        # print(c0, c1)
        ans += c0 + c1
    print(ans)
