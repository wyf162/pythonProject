# -*- coding: utf-8 -*-
# @Time: 2024/3/26 15:20
# @Author: yfwang
# @File: 1783C.py
# https://codeforces.com/problemset/problem/1783/C

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
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
    n, m = MI()
    a = LI()
    b = sorted(a)
    k = 0
    for x in b:
        if m >= x:
            m -= x
            k += 1
        else:
            break

    if 0 < k < n and m + b[k - 1] >= a[k]:
        k += 1

    print(n - k + 1)
