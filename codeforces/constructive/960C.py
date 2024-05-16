# -*- coding: utf-8 -*-
# @Time: 2024/5/16 9:32
# @Author: yfwang
# @File: 960C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    X, d = MI()
    gap = d + d
    d = 32
    nums = []
    st = 1
    while X:
        # print(X)
        if X >= (2 ** d - 1):
            nums.extend([st for i in range(d)])
            st += gap
            X -= 2 ** d - 1
        else:
            d -= 1
    print(len(nums))
    print(*nums)
