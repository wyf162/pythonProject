# -*- coding: utf-8 -*-
# @Time: 2024/7/3 14:35
# @Author: yfwang
# @File: 1930D1.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


def f(nums):
    n = len(nums)
    dp = [n] * n
    for i in range(n):
        if nums[i] == 1:
            if i - 3 >= 0:
                dp[i] = min(dp[i], dp[i - 3] + 1)
            else:
                dp[i] = min(dp[i], 1)
            if i - 2 >= 0:
                dp[i] = min(dp[i], dp[i - 2] + 1)
            else:
                dp[i] = min(dp[i], 1)

            if i - 1 >= 0:
                dp[i] = min(dp[i], dp[i - 1] + 1)
            else:
                dp[i] = min(dp[i], 1)

        else:
            if i - 1 >= 0:
                dp[i] = dp[i - 1]
            else:
                dp[i] = 0
    # print(nums)
    # print(dp)
    return dp[-1]


# nums = [1, 1, 1, 1, 0, 1, 1]
# nums = [0, 1]
# ret = f(nums)
# print(ret)

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    s = [int(x) for x in input()]
    tot = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            t = s[i:j]
            tot += f(t)

    print(tot)
