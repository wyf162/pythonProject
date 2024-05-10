# -*- coding: utf-8 -*-
# @Time: 2024/5/10 14:16
# @Author: yfwang
# @File: 1555C.py

import sys
from itertools import accumulate

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
    nums1 = LI()
    nums2 = LI()
    pre_sum1 = list(accumulate(nums1, initial=0))
    pre_sum2 = list(accumulate(nums2, initial=0))
    ans = 0x3f3f3f3f
    for i in range(n):
        ans = min(ans, max(pre_sum1[-1] - pre_sum1[i + 1], pre_sum2[i]))
    print(ans)
