# -*- coding: utf-8 -*-
# @Time: 2024/7/18 10:09
# @Author: yfwang
# @File: 622C.py

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
inf = 10 ** 6
N = 10 ** 6 + 5

tcn = 1
for _tcn_ in range(tcn):
    n, q = MI()
    A = LI()
    nex = [n for i in range(n)]

    i1, i2 = n - 1, n - 1
    for i in range(n - 2, -1, -1):
        if A[i] != A[i1]:
            nex[i] = i1
            i1, i2 = i, i1
        elif A[i] != A[i2]:
            nex[i] = i2
            i1 = i

    for _ in range(q):
        L, R, X = MI()
        L, R = L - 1, R - 1
        if A[L] != X:
            print(L + 1)
        elif nex[L] <= R:
            print(nex[L] + 1)
        else:
            print(-1)
