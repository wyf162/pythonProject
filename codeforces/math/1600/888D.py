# -*- coding : utf-8 -*-
# @Time: 2024/8/2 21:10
# @Author: yefei.wang
# @File: 888D.py

import math
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

A = [1, 1, 1, 2, 9]

tcn = 4
for _tcn_ in range(tcn):
    n, k = MI()
    tot = 1
    for i in range(2, k + 1):
        tot += math.comb(n, i) * A[i]
    print(tot)
