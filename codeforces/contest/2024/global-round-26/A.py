# -*- coding : utf-8 -*-
# @Time: 2024/6/9 22:32
# @Author: yefei.wang
# @File: A.py

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
    n = I()
    A = LI()
    if A[0] == A[-1]:
        print('NO')
    else:
        print('YES')
        if A[0] == A[-2]:
            print('R' + 'B' * (n - 1))
        else:
            print('R' * (n - 1) + 'B')
