# -*- coding: utf-8 -*-
# @Time: 2024/3/14 17:23
# @Author: yfwang
# @File: 1809D.py
# https://codeforces.com/problemset/problem/1809/D

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

cost1 = 10 ** 12
cost2 = 10 ** 12 + 1
tcn = I()
for _tcn_ in range(tcn):
    ss = list(input())
    n = len(ss)
    dp0 = [1 << 63] * (n + 1)
    dp1 = [1 << 63] * (n + 1)

    dp0[0] = dp1[0] = 0

    for i in range(n):
        if ss[i] == '0':
            dp0[i + 1] = min(dp0[i + 1], dp0[i])
            dp1[i + 1] = min(dp1[i + 1], dp0[i])
            dp1[i + 1] = min(dp1[i + 1], dp1[i] + cost2)
        else:
            dp0[i + 1] = min(dp0[i + 1], dp0[i] + cost2)
            dp1[i + 1] = min(dp1[i + 1], dp1[i])

        if i + 1 < n and ss[i] == '1' and ss[i + 1] == '0':
            dp1[i + 2] = min(dp1[i + 2], dp0[i] + cost1)

    print(dp1[-1])
