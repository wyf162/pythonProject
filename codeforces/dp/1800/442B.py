# -*- coding: utf-8 -*-
# @Time: 2024/7/16 10:06
# @Author: yfwang
# @File: 442B.py
# probabilities

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

tcn = 2
for _tcn_ in range(tcn):
    n = I()
    probs = [float(x) for x in input().split()]
    probs.sort(reverse=True)

    p0, p1 = 1, 0
    ans = 0

    for p in probs:
        p1 = p1 * (1 - p) + p0 * p
        p0 *= 1 - p
        ans = max(ans, p1)

    print(ans)
