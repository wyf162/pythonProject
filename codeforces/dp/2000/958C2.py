# -*- coding: utf-8 -*-
# @Time: 2024/6/13 13:16
# @Author: yfwang
# @File: 958C2.py

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



n, k, p = MI()
nums = [x % p for x in MI()]
acc = list(accumulate(nums, initial=0))

dp = [0] * k
idx = [0] * k

for i in range(1, n):
    for j in range(k - 1, 0, -1):
        if dp[j - 1] + (acc[i] - acc[idx[j - 1]]) % p > dp[j]:
            dp[j] = dp[j - 1] + (acc[i] - acc[idx[j - 1]]) % p
            idx[j] = i

print(dp[k - 1] + (acc[-1] - acc[idx[k - 1]]) % p)
