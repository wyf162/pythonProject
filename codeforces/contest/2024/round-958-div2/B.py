# -*- coding : utf-8 -*-
# @Time: 2024/7/15 22:39
# @Author: yefei.wang
# @File: B.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
    s = [int(x) for x in input()]
    nums = []
    for i in range(n):
        if s[i] == 1:
            nums.append(1)
        else:
            if nums and nums[-1] == 0:
                continue
            else:
                nums.append(0)
    c0, c1 = nums.count(0), nums.count(1)
    YN(c0 < c1)
