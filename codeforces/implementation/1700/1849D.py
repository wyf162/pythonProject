# -*- coding: utf-8 -*-
# @Time: 2024/7/3 9:00
# @Author: yfwang
# @File: 1849D.py

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

tcn = 3
for _tcn_ in range(tcn):
    n = I()
    A = [0] + LI() + [0]
    ans = 0
    for i in range(1, n + 1):
        if A[i - 1] != 0:
            A[i - 1] -= 1
        elif A[i] == 0 and A[i + 1] != 0:
            A[i + 1] -= 1
        else:
            ans += 1
    print(ans)
