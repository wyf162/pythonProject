# -*- coding: utf-8 -*-
# @Time: 2024/3/19 16:04
# @Author: yfwang
# @File: A.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
    a, c, b = MI()
    if c % 3 == 0:
        ans = a + (b + 2) // 3 + c // 3
    if c % 3 == 1:
        if b <= 1:
            ans = -1
        else:
            ans = a + (b + c + 2) // 3
    if c % 3 == 2:
        if b <= 0:
            ans = -1
        else:
            ans = a + (b + c + 2) // 3

    print(ans)
