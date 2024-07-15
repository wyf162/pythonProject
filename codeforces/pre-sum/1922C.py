# -*- coding: utf-8 -*-
# @Time: 2024/7/15 13:07
# @Author: yfwang
# @File: 1922C.py

import sys
from itertools import accumulate

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    q = I()
    queries = [LGMI() for _ in range(q)]

    L = [1] * n
    for i in range(1, n - 1):
        if abs(A[i] - A[i - 1]) < abs(A[i + 1] - A[i]):
            L[i] = abs(A[i + 1] - A[i])
    R = [1] * n
    for i in range(n - 2, 0, -1):
        if abs(A[i] - A[i - 1]) > abs(A[i + 1] - A[i]):
            R[i] = abs(A[i] - A[i - 1])

    # print(L)
    PL = list(accumulate(L, initial=0))
    # print(R)
    PR = list(accumulate(R, initial=0))

    for u, v in queries:
        if u < v:
            ans = PL[v] - PL[u]
        else:
            ans = PR[u + 1] - PR[v + 1]
        print(ans)
