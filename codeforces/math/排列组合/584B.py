# -*- coding: utf-8 -*-
# @Time: 2024/5/27 13:26
# @Author: yfwang
# @File: 584B.py
# https://codeforces.com/problemset/problem/584/B
# 排列组合 容斥原理

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

tcn = 2
for _tcn_ in range(tcn):
    n = I()
    ans = pow(27, n, mod) - pow(7, n, mod)
    ans %= mod
    print(ans)
