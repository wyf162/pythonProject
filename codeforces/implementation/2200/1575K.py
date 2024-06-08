# -*- coding : utf-8 -*-
# @Time: 2024/6/8 11:16
# @Author: yefei.wang
# @File: 1575K.py

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

tcn = 5
for _tcn_ in range(tcn):
    n, m, k, r, c = MI()
    x1, y1, x2, y2 = MI()
    if x1 == x2 and y1 == y2:
        ans = pow(k, n * m, mod)
    else:
        ans = pow(k, n * m - r * c, mod)
    print(ans)
