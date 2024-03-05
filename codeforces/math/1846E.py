# -*- coding: utf-8 -*-
# @Time: 2024/3/5 17:10
# @Author: yfwang
# @File: 1846E.py
# https://codeforces.com/problemset/status/1846/problem/E2

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    ans = False
    for p in range(2, 100):
        x = int(n ** (1 / p))
        for l in range(max(2, x - 2), x + 10):
            if (l ** (p + 1) - 1) // (l - 1) == n:
                ans = True
                break
    YN(ans)
