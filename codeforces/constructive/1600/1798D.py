# -*- coding : utf-8 -*-
# @Time: 2024/5/21 10:05
# @Author: yefei.wang
# @File: 1798D.py
# https://codeforces.com/problemset/problem/1798/D

import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    a.sort()
    mi, mx = a[0], a[-1]
    if mi == mx:
        print('No')
    else:
        print('Yes')
        b = []
        s = 0
        i = 0
        j = n - 1
        while i <= j:
            if s >= 0:
                b.append(a[i])
                s += a[i]
                i += 1
            else:
                b.append(a[j])
                s += a[j]
                j -= 1
        print(*b)
