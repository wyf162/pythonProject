# -*- coding : utf-8 -*-
# @Time: 2024/4/7 13:19
# @Author: yefei.wang
# @File: 1841D.py
# https://codeforces.com/contest/1841/problem/D

import sys
from math import inf

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    intervals = [LI() for _ in range(n)]
    intervals.sort(key=lambda x: x[1])
    last = -inf
    right = None
    cnt = 0
    for l, r in intervals:
        if l > last:
            if right is None:
                right = r
            else:
                if l <= right:
                    cnt += 1
                    last = r
                    right = None
                else:
                    right = r
    print(n - cnt * 2)
