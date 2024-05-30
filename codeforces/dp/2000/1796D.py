# -*- coding: utf-8 -*-
# @Time: 2024/5/30 8:58
# @Author: yfwang
# @File: 1796D.py

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
    n, k, x = MI()
    A = LI()
    f = [[-inf for _ in range(k + 1)] for _ in range(n + 1)]
    f[0][0] = 0
    for i in range(n):
        f[i + 1][0] = max(f[i][0] + A[i] - x, 0)
        for j in range(1, k + 1):
            f[i + 1][j] = max(f[i][j - 1] + A[i] + x, f[i][j] + A[i] - x)
            if j <= i + 1:
                f[i + 1][j] = max(f[i + 1][j], 0)

    ans = -inf
    for i in range(n - k):
        ans = max(ans, max(f[i]))
    for i in range(n - k, n + 1):
        ans = max(ans, max(f[i][i - (n - k):]))
    print(ans)
