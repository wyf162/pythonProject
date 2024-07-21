# -*- coding : utf-8 -*-
# @Time: 2024/7/20 23:58
# @Author: yefei.wang
# @File: D.py

import copy
import sys
from collections import Counter

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
    cover = 0
    tot = 0
    for i in range(n):
        if A[i] <= cover:
            continue
        if A[i] >= 5:
            tot += 1


