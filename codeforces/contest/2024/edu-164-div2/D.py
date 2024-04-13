# -*- coding : utf-8 -*-
# @Time: 2024/4/12 23:03
# @Author: yefei.wang
# @File: D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
nums.sort()

ans = 0
N = 5005
dp = [0] * N
dp[0] = 1
tot = 0
for i in range(n):
    for j in range(N):
        if j <= nums[i]:
            ans += dp[j] * nums[i]
        else:
            ans += dp[j] * ((nums[i] + j + 1) // 2)
        ans %= mod2
    if tot:
        ans += tot + nums[i] // 2
        ans %= mod2

    ndp = [0] * N
    ntot = 0
    for j in range(N):
        if j + nums[i] < N:
            ndp[j + nums[i]] += dp[j]
            ndp[j + nums[i]] %= mod2
        elif dp[j]:
            ntot += dp[j] * ((j + nums[i] + 1) // 2)
            ntot %= mod2

    for j in range(N):
        ndp[j] += dp[j]
        ndp[j] %= mod2
    ntot += tot

    dp = ndp
    tot = ntot
    tot %= mod2
print(ans)
