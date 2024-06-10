# -*- coding : utf-8 -*-
# @Time: 2024/6/10 9:16
# @Author: yefei.wang
# @File: 1364B.py

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    P = LI()
    nums = []
    for x in P:
        if len(nums) < 2:
            nums.append(x)
        else:
            if nums[-2] < nums[-1] < x:
                nums[-1] = x
            elif nums[-2] > nums[-1] > x:
                nums[-1] = x
            else:
                nums.append(x)
    print(len(nums))
    print(*nums)
