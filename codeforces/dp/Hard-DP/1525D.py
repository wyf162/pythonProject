# -*- coding: utf-8 -*-
# @Time: 2024/4/29 17:15
# @Author: yfwang
# @File: 1525D.py

import sys
from math import inf

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

n = I()
nums = LI()
pos0, pos1 = [], []
for i in range(n):
    if nums[i]:
        pos1.append(i)
    else:
        pos0.append(i)
x, y = len(pos0), len(pos1)
dp = [[inf] * (y + 1) for _ in range(x + 1)]
dp[0][0] = 0
for i in range(1, x + 1):
    for j in range(y, -1, -1):
        dp[i][j] = dp[i - 1][j]
        if j: dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + abs(pos0[i - 1] - pos1[j - 1]))
print(dp[-1][-1])
