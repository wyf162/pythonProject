# -*- coding: utf-8 -*-
# @Time: 2024/7/11 16:14
# @Author: yfwang
# @File: demo_zfunc.py

def z_func(s):
    z = [0] * len(s)
    left, right = 0, 0
    for i in range(1, len(s)):
        z[i] = max(0, min(z[i - left], right - i))
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


n = 6
nums = [1, 2, 3, 4, 3, 4]
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    z = z_func(nums[i:])
    for L in range(1, n // 2 + 1):
        if i + L >= n:
            break
        if z[L] < L and i + z[L] + L < n and nums[i + z[L]] < nums[i + z[L] + L]:
            dp[i][L] = 1

for i in range(n):
    print(dp[i])
