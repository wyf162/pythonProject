# -*- coding : utf-8 -*-
# @Time: 2023/10/8 13:19
# @Author: yefei.wang
# @File: e.py

import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, x = MI()
t = LI()
mod = 998244353

dp = [0] * (x + 1)
dp[0] = 1
pow_n = pow(n, -1, mod)

for i in range(x):
    for j in t:
        if i + j <= x:
            dp[i + j] += dp[i] * pow_n
            dp[i + j] %= mod
ans = 0
start = max(0, x - t[0] + 1)

for i in range(start, x + 1):
    ans += dp[i]

ans = ans * pow_n % mod
print(ans)
