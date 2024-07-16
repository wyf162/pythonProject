# -*- coding: utf-8 -*-
# @Time: 2024/7/16 10:57
# @Author: yfwang
# @File: 1157D.py

import math
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
inf = 0x3f3f3f3f

tcn = 1
for _tcn_ in range(tcn):
    n, k = MI()
    nums = []

    tot = n
    for i in range(k, 0, -1):
        if i > 30:
            if not nums:
                nums.append(1)
            else:
                nums.append(nums[-1] + 1)
        else:
            q = ((1 << i) - 1)
            x = math.ceil(tot / q)
            if not nums:
                nums.append(max(x, 1))
            else:
                if x <= nums[-1]:
                    nums.append(nums[-1] + 1)
                else:
                    nums.append(min(x, nums[-1] * 2))
        tot -= nums[-1]

    tot = sum(nums)
    if tot == n:
        YN(True)
        print(*nums)
    else:
        YN(False)
