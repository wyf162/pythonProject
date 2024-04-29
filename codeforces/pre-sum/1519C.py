# -*- coding: utf-8 -*-
# @Time: 2024/4/29 14:24
# @Author: yfwang
# @File: 1519C.py

import sys
from itertools import accumulate

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    n = I()
    nums1 = LI()
    nums2 = LI()
    groups = [[] for _ in range(n+1)]
    for u, s in zip(nums1, nums2):
        groups[u].append(s)

    mx = 0
    for group in groups:
        mx = max(len(group), mx)
        group.sort()

    ans = [0] * (n + 1)
    for group in groups:
        m = len(group)
        pre_sum = list(accumulate(group, initial=0))
        tot = pre_sum[m]
        for k in range(1, m + 1):
            ans[k] += tot - pre_sum[m % k]
    print(*ans[1:])

