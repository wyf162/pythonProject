# -*- coding : utf-8 -*-
# @Time: 2024/3/6 23:04
# @Author: yefei.wang
# @File: F.py

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
    L, R = MI()
    if L % 2 == 0 and R % 2 == 0:
        print(-1)
        continue
    A = list(range(L, R + 1))
    n = len(A)
    if n % 2 == 0:
        B = []
        for i in range(0, n, 2):
            B.append(A[i + 1])
            B.append(A[i])
    else:
        B = []
        for i in range(0, n - 3, 2):
            B.append(A[i + 1])
            B.append(A[i])
        B.append(A[-1])
        B.append(A[-3])
        B.append(A[-2])

    print(*[str(x) for x in B])
