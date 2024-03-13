# -*- coding: utf-8 -*-
# @Time: 2024/3/11 9:44
# @Author: yfwang
# @File: 1845D.py
# https://codeforces.com/problemset/problem/1845/D


import sys
from math import inf

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
    nums = LI()
    nums = [0] + nums
    n += 1

    pre_sum = [0] * n
    pre_sum[0] = nums[0]
    for i in range(1, n):
        pre_sum[i] = pre_sum[i - 1] + nums[i]

    suf_sum = [-1] * n
    suf_sum[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        suf_sum[i] = suf_sum[i + 1] + nums[i]

    best = -1
    mx = -inf
    b = -1
    for i in range(n - 1, -1, -1):
        ans = pre_sum[i] + b
        b = max(b, suf_sum[i])
        if ans > mx:
            mx = ans
            best = pre_sum[i]
    print(best)
