# -*- coding: utf-8 -*-
# @Time: 2024/6/14 13:55
# @Author: yfwang
# @File: 1980E.py

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

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    A = [LI() for _ in range(n)]
    B = [LI() for _ in range(n)]

    A1 = sorted(sorted(x) for x in A)
    B1 = sorted(sorted(x) for x in B)
    A2 = sorted(sorted(x) for x in zip(*A))
    B2 = sorted(sorted(x) for x in zip(*B))

    if A1 == B1 and A2 == B2:
        print("YES")
    else:
        print("NO")


