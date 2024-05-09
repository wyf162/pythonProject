# -*- coding: utf-8 -*-
# @Time: 2024/5/9 17:40
# @Author: yfwang
# @File: 148D.py

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
    N, M = MI()
    dp0 = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
    dp1 = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
    dp2 = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
    dp2[N][M] = 1
    dragon = princess = 0
    stk = [(N, M)]
    while stk:
        n, m = stk.pop()
        princess += dp2[n][m] * n / (n + m)
        dp0[n][m - 1] += dp2[n][m] + m / (n + m)

        dragon += dp0[n][m - 1] * n / (n + m - 1)
        dp1[n][m - 2] = dp0[n][m] * m / (n + m - 1)

        dp2[n - 1][m - 2] += dp1[n][m - 2] * n / (n + m - 2)
        dp2[n][m - 3] += dp1[n][m - 2] * m / (n + m - 2)

        stk.append((n - 1, m - 2))
        stk.append((n, m - 3))

    print(princess)
