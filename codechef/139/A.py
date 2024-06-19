# -*- coding : utf-8 -*-
# @Time: 2024/6/19 22:31
# @Author: yefei.wang
# @File: A.py

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
    n, c = MI()
    A = LI()
    A1 = A[:1]
    A2 = A[1:]
    A2.sort()
    while A2:
        if sum(A1) * sum(A2) <= c:
            break
        else:
            A1.append(A2.pop())
    print(len(A1))
