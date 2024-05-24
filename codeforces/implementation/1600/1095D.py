# -*- coding: utf-8 -*-
# @Time: 2024/5/24 10:21
# @Author: yfwang
# @File: 1095D.py

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


tcn = 1
for _tcn_ in range(tcn):
    n = I()
    g = [LGMI() for _ in range(n)]
    if n == 3:
        ans = [0, 1, 2]
    else:
        ans = [0]
        for _ in range(n - 1):
            i = ans[-1]
            i1, i2 = g[i]
            x1, y1 = g[i1]
            x2, y2 = g[i2]

            if i1 in (x1, y1, x2, y2):
                ans.append(i2)
            else:
                ans.append(i1)
    print(' '.join(str(x + 1) for x in ans))
