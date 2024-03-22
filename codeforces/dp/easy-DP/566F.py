# -*- coding: utf-8 -*-
# @Time: 2024/3/22 9:24
# @Author: yfwang
# @File: 566F.py
# https://codeforces.com/problemset/problem/566/F

import sys

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
cnt = [0] * (10 ** 6 + 1)
for num in nums:
    cnt[num] += 1

dp = [0] * (10 ** 6 + 1)
for i in range(1, 10 ** 6 + 1):
    dp[i] += cnt[i]
    for j in range(i, 10 ** 6 + 1, i):
        dp[j] = max(dp[j], dp[i])

print(max(dp))
