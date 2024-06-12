# -*- coding: utf-8 -*-
# @Time: 2024/6/12 9:18
# @Author: yfwang
# @File: G.py

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
    L, R, K = MI()
    if K >= 10:
        print(0)
        continue
    c = 9 // K
    ans1 = c * (pow(c + 1, R, mod) - 1) * pow(c, -1, mod) % mod
    ans2 = c * (pow(c + 1, L, mod) - 1) * pow(c, -1, mod) % mod

    ans = ans1 - ans2
    ans %= mod
    print(ans)
