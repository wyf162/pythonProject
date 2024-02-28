# -*- coding: utf-8 -*-
# @Time: 2024/2/28 10:55
# @Author: yfwang
# @File: 1862F.py
# https://codeforces.com/problemset/problem/1862/F

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
    d, f = MI()
    n = I()
    nums = LI()

    tot = sum(nums)
    dp = [0] * (tot + 1)
    dp[0] = True
    for i in range(n):
        for w in range(tot, nums[i] - 1, -1):
            dp[w] = dp[w] | dp[w - nums[i]]

    ans = 2e9
    for i in range(tot + 1):
        if dp[i]:
            ans = min(ans, max((i + d - 1) // d, (tot - i + f - 1) // f))
    print(ans)
