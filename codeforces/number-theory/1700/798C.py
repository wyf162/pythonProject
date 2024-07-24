# -*- coding: utf-8 -*-
# @Time: 2024/7/24 13:49
# @Author: yfwang
# @File: 798C.py
# gcd

import sys
import math

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
    n = I()
    A = LI()
    x = 0
    for i in range(n):
        x = math.gcd(x, A[i])
    if x > 1:
        print('YES')
        print(0)
        continue

    ans = 0
    for i in range(n):
        if A[i] % 2:
            if i + 1 < n and A[i + 1] % 2:
                A[i + 1] = 0
                ans += 1
            else:
                ans += 2
    print('YES')
    print(ans)
