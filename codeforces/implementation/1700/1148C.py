# -*- coding: utf-8 -*-
# @Time: 2024/5/29 9:18
# @Author: yfwang
# @File: 1148C.py
# permutation

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
    P = LGMI()
    # Q = copy.deepcopy(P)
    ind = [0] * n
    for i, x in enumerate(P):
        ind[x] = i
    ops = []
    for i in range(n):
        x = ind[i]
        if i == x:
            continue
        ind[P[i]], ind[P[x]] = x, i
        P[i], P[x] = P[x], P[i]

        if abs(i - x) * 2 >= n:
            ops.append((i, x))
        else:
            if abs(i - 0) * 2 >= n and abs(n - 1 - x) * 2 >= n:
                ops.append((i, 0))
                ops.append((0, n - 1))
                ops.append((n - 1, x))
                ops.append((n - 1, 0))
                ops.append((0, i))
            elif abs(n - 1 - i) * 2 >= n and abs(x - 0) * 2 >= n:
                ops.append((i, n - 1))
                ops.append((n - 1, 0))
                ops.append((0, x))
                ops.append((0, n - 1))
                ops.append((n - 1, i))
            elif abs(i - 0) * 2 >= n and abs(x - 0) * 2 >= n:
                ops.append((i, 0))
                ops.append((0, x))
                ops.append((0, i))
            elif abs(n - 1 - i) * 2 >= n and abs(n - 1 - x) * 2 >= n:
                ops.append((i, n - 1))
                ops.append((n - 1, x))
                ops.append((n - 1, i))
    print(len(ops))
    for i in range(len(ops)):
        print(ops[i][0] + 1, ops[i][1] + 1)

    # for i, j in ops:
    #     Q[i], Q[j] = Q[j], Q[i]
    # print(Q)
