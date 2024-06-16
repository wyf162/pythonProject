# -*- coding : utf-8 -*-
# @Time: 2024/6/16 13:47
# @Author: yefei.wang
# @File: 1396A.py

import copy
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
    A = LI()
    if n == 1:
        print(1, 1)
        print(-A[0])
        print(1, 1)
        print(0)
        print(1, 1)
        print(0)
    else:
        print(1, 1)
        print(-A[0])
        print(2, n)
        print(*[x * (n - 1) for x in A[1:]])
        print(1, n)
        rets = [0] + [-x * n for x in A[1:]]
        print(*rets)
