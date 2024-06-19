# -*- coding: utf-8 -*-
# @Time: 2024/6/19 16:31
# @Author: yfwang
# @File: 1221D.py

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
inf = 10 ** 18

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = []
    B = []
    for _ in range(n):
        a, b = MI()
        A.append(a)
        B.append(b)

    f = [[inf, inf, inf] for _ in range(n)]
    f[0][0] = 0
    f[0][1] = B[0]
    f[0][2] = B[0] + B[0]
    for i in range(1, n):
        if A[i - 1] == A[i]:
            f[i][0] = min(f[i - 1][1], f[i - 1][2])
            f[i][1] = min(f[i - 1][0], f[i - 1][2]) + B[i]
            f[i][2] = min(f[i - 1][0], f[i - 1][1]) + B[i] + B[i]
        elif A[i - 1] + 1 == A[i]:
            f[i][0] = min(f[i - 1][0], f[i - 1][2])
            f[i][1] = min(f[i - 1][0], f[i - 1][1]) + B[i]
            f[i][2] = min(f[i - 1][0], f[i - 1][1], f[i - 1][2]) + B[i] + B[i]
        elif A[i - 1] + 2 == A[i]:
            f[i][0] = min(f[i - 1][0], f[i - 1][1])
            f[i][1] = min(f[i - 1][0], f[i - 1][1], f[i - 1][2]) + B[i]
            f[i][2] = min(f[i - 1][0], f[i - 1][1], f[i - 1][2]) + B[i] + B[i]
        elif A[i - 1] == A[i] + 1:
            f[i][0] = min(f[i - 1][0], f[i - 1][1], f[i - 1][2])
            f[i][1] = min(f[i - 1][1], f[i - 1][2]) + B[i]
            f[i][2] = min(f[i - 1][0], f[i - 1][2]) + B[i] + B[i]
        elif A[i - 1] == A[i] + 2:
            f[i][0] = min(f[i - 1][0], f[i - 1][1], f[i - 1][2])
            f[i][1] = min(f[i - 1][0], f[i - 1][1], f[i - 1][2]) + B[i]
            f[i][2] = min(f[i - 1][1], f[i - 1][2]) + B[i] + B[i]
        else:
            f[i][0] = min(f[i - 1][0], f[i - 1][1], f[i - 1][2])
            f[i][1] = min(f[i - 1][0], f[i - 1][1], f[i - 1][2]) + B[i]
            f[i][2] = min(f[i - 1][0], f[i - 1][1], f[i - 1][2]) + B[i] + B[i]

    ans = min(f[n - 1])
    print(ans)
