# -*- coding : utf-8 -*-
# @Time: 2024/7/10 23:20
# @Author: yefei.wang
# @File: D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 0x3f3f3f3f

tcn = I()
for _tcn_ in range(tcn):
    n, x = MI()
    mx = 10 ** x - 1
    A = LI()
    AX = [(a, i) for i, a in enumerate(A)]
    AX.sort()
    B = [ax[0] for ax in AX]
    C = [ax[1] for ax in AX]

