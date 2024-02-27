# -*- coding: utf-8 -*-
# @Time: 2024/2/27 13:14
# @Author: yfwang
# @File: 1875D.py

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    cnt = [0] * n
    for num in nums:
        if num < n:
            cnt[num] += 1
    mex = 0
    for i in range(n):
        if cnt[i]:
            mex = i + 1
        else:
            break
    dp = [1 << 60] * (n+1)
    for i in range(mex):
        dp[i] = (cnt[i] - 1) * mex
    dp[mex] = 0
    for i in range(n, -1, -1):
        now = dp[i]
        for j in range(i-1, -1, -1):
            dp[j] = min(dp[j], now+cnt[j] * i)
    print(dp[0])
