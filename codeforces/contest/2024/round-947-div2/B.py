# -*- coding : utf-8 -*-
# @Time: 2024/5/25 23:07
# @Author: yefei.wang
# @File: B.py

import math
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
    A.sort()
    if 1 in A:
        YN(True)
        continue
    vis = [0] * n
    vis[0] = 1
    x1 = A[0]
    x2 = 0
    for i in range(n):
        if A[i] % x1 == 0:
            vis[i] = 1
        elif x2 == 0:
            x2 = A[i]
    if x2 == 0:
        YN(True)
        continue
    for i in range(n):
        if A[i] % x2 == 0:
            vis[i] = 1
    YN(sum(vis) == n)
