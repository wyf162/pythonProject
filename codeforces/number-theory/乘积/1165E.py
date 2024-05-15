# -*- coding: utf-8 -*-
# @Time: 2024/5/15 9:04
# @Author: yfwang
# @File: 1165E.py
# https://codeforces.com/problemset/problem/1165/E

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
mod = 998244353

tcn = 3
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    B = LI()
    for i in range(n):
        A[i] *= (i - 0 + 1) * (n - i)
    A.sort()
    B.sort(reverse=True)
    tot = 0
    for a, b in zip(A, B):
        tot += a * b
        tot %= mod
    print(tot)
