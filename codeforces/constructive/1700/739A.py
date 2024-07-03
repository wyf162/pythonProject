# -*- coding: utf-8 -*-
# @Time: 2024/7/3 9:57
# @Author: yfwang
# @File: 739A.py
# mex

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
    n, m = MI()
    segments = [LI() for _ in range(m)]
    mi = n
    for start, end in segments:
        mi = min(mi, end - start + 1)
    nums = list(range(mi))
    rets = nums * ((n + mi - 1) // mi)
    print(mi)
    print(*rets[:n])

