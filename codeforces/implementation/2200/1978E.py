# -*- coding: utf-8 -*-
# @Time: 2024/6/17 9:55
# @Author: yfwang
# @File: 1978E.py

import copy
import sys
from itertools import accumulate


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
    s0 = [int(x) for x in input()]
    t0 = [int(x) for x in input()]
    q = I()
    queries = [LGMI() for _ in range(q)]
    t1 = t0[:]
    for i in range(1, n - 1):
        if s0[i - 1] == 0 and s0[i + 1] == 0:
            t1[i] = 1

    s1 = s0[:]
    for i in range(1, n - 1):
        if t1[i - 1] == 1 and t1[i + 1] == 1:
            s1[i] = 1
    acc0 = list(accumulate(s1, initial=0))

    for qry in queries:
        L, R = qry
        if R - L >= 3:
            ret = acc0[R - 1] - acc0[L+2]
            ret += s0[L] + s0[R]
            ret += s0[L + 1] | (t0[L] & t1[L + 2])
            ret += s0[R - 1] | (t0[R] & t1[R - 2])
            print(ret)
        else:
            x1 = s0[L:R + 1]
            x2 = t0[L:R + 1]
            k = len(x1)
            for i in range(1, k - 1):
                if x1[i - 1] == 0 and x1[i + 1] == 0:
                    x2[i] = 1
            for i in range(1, k - 1):
                if x2[i - 1] and x2[i + 1]:
                    x1[i] = 1
            ret = sum(x1)
            print(ret)
