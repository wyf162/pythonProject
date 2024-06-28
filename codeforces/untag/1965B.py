# -*- coding: utf-8 -*-
# @Time: 2024/6/28 16:55
# @Author: yfwang
# @File: 1965B.py

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

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    x = k.bit_length() - 1
    nums = []
    for i in range(20):
        if i == x:
            nums.append(k - (1 << i))
            nums.append(k + 1)
            nums.append(k + 1 + (1 << i))
        else:
            nums.append(1 << i)
    print(len(nums))
    print(*nums)
