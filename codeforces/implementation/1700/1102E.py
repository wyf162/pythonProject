# -*- coding: utf-8 -*-
# @Time: 2024/5/8 9:09
# @Author: yfwang
# @File: 1102E.py

import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 3
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    hst = defaultdict(list)
    for i, a in enumerate(A):
        hst[a].append(i)
    nums = []
    right = 0
    for i in range(n):
        right = max(right, hst[A[i]][-1])
        if i >= right:
            nums.append(right)
            right = i + 1
    # print(nums)
    m = len(nums)
    dp = [0] * m
    dp[0] = 1
    for i in range(1, m):
        dp[i] = 2 * dp[i-1]
        dp[i] %= mod2
    print(dp[-1])
