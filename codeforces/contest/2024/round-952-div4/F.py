# -*- coding: utf-8 -*-
# @Time: 2024/6/12 9:05
# @Author: yfwang
# @File: F.py

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
    h, n = MI()
    A = LI()
    C = LI()

    L, R = 1, 10 ** 18
    while L <= R:
        mid = (L + R) // 2
        tot = 0
        for i, c in enumerate(C):
            tot += A[i] * ((mid - 1) // c + 1)

        if tot >= h:
            ans = mid
            R = mid - 1
        else:
            L = mid + 1

    print(ans)
