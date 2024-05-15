# -*- coding: utf-8 -*-
# @Time: 2024/5/15 13:27
# @Author: yfwang
# @File: 1644D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
sys.stdout = open('../../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, m, k, q = MI()
    query = [TI() for i in range(q)]
    row = set()
    column = set()
    res = 1
    for x, y in query[::-1]:
        if (x not in row) or (y not in column):
            res = res * k % mod
        row.add(x)
        column.add(y)
        if len(row) == n or len(column) == m:
            break

    print(res)

