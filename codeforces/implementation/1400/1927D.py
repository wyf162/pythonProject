# -*- coding: utf-8 -*-
# @Time: 2024/7/8 9:00
# @Author: yfwang
# @File: 1927D.py

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
    n = I()
    A = LI()
    q = I()
    queries = [LGMI() for _ in range(q)]
    B = [i for i in range(n)]
    cur = n-1
    for i in range(n-1, -1, -1):
        if A[i] == A[cur]:
            B[i] = cur
        else:
            cur = i

    for l, r in queries:
        if B[l] < r:
            print(l + 1, B[l] + 2)
        else:
            print(-1, -1)
    print()