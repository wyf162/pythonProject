# -*- coding: utf-8 -*-
# @Time: 2024/6/26 10:44
# @Author: yfwang
# @File: 1009E.py
# probabilities

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

tcn = 1
for _tcn_ in range(tcn):
    n = I()
    A = LI()

    pow2 = [1] * (n + 1)
    for i in range(n):
        pow2[i+1] = pow2[i] * 2 % mod

    ans = 0
    for i in range(n):
        ans += A[i] * (pow2[n - i - 1] + (n - i - 1) * pow2[n - i - 2]) % mod
        ans %= mod

    print(ans)
