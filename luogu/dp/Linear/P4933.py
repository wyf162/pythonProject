# -*- coding : utf-8 -*-
# @Time: 2023/10/3 20:55
# @Author: yefei.wang
# @File: P4933.py


import sys
from collections import Counter

sys.stdin = open('./../../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
nums = LI()
mod = 998244353

dp = [Counter() for _ in range(n)]
rst = 0
for i in range(1, n):
    for j in range(i):
        k = nums[i] - nums[j]
        dp[i][k] += dp[j][k] + 1
for i in range(1, n):
    for k, v in dp[i].items():
        rst += v
rst += n
rst %= mod
print(rst)
