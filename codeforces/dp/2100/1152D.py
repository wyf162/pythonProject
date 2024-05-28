# -*- coding: utf-8 -*-
# @Time: 2024/5/24 16:05
# @Author: yfwang
# @File: 1152D.py
# parenthesis trie

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
    f = [[0 for _ in range(n + 1)] for _ in range(2 * n + 1)]
    g = [[0 for _ in range(n + 1)] for _ in range(2 * n + 1)]

    f[0][0] = 0
    g[0][0] = 1

    for i in range(1, n * 2 + 1):
        for j in range(0, n + 1):
            ret = 0
            flag = 0
            if j > 0:
                ret += f[i - 1][j - 1] % mod
                flag |= g[i - 1][j - 1]
            if j + 1 <= min(n, i - 1):
                ret += f[i - 1][j + 1] % mod
                flag |= g[i - 1][j + 1]
            if flag:
                f[i][j] = (ret + 1) % mod
                g[i][j] = 0
            else:
                f[i][j] = ret
                g[i][j] = 1

    print(f[n * 2][0])
