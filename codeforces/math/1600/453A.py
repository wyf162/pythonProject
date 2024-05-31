# -*- coding: utf-8 -*-
# @Time: 2024/5/31 16:12
# @Author: yfwang
# @File: 453A.py
# 容斥原理

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

tcn = 3
for _tcn_ in range(tcn):
    m, n = MI()
    if n == 1:
        print((m + 1) / 2)
    else:
        ans = 0
        pre = 0
        # pp = []
        for x in range(1, m + 1):
            cur = pow(x / m, n)
            p = cur - pre
            ans += x * p
            # pp.append(p)
            pre = cur
        # print(pp)
        print(ans)
