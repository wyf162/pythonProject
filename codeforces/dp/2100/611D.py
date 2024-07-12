# -*- coding: utf-8 -*-
# @Time: 2024/7/11 13:25
# @Author: yfwang
# @File: 611D.py


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


mod = 1000000007

n = int(input())
nums = [int(x) for x in input()]
f = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n):
    z = z_func(nums[i:])
    for L in range(1, n // 2 + 1):
        if i + L >= n:
            break
        if z[L] < L and i + z[L] + L < n and nums[i + z[L]] < nums[i + z[L] + L]:
            f[i][L] = 1

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
pre_sum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for k in range(1, n + 1):
    for j in range(k):
        if nums[j] == 0:
            pre_sum[k][j + 1] = pre_sum[k][j] + dp[j][k]
            continue

        if j == 0:
            dp[j][k] = 1
        else:
            i = max(j - (k - j), -1)
            if k - j == j - i and f[i][k - j]:
                dp[j][k] += dp[i][j]
                dp[j][k] %= mod
            if i + 1 < j:
                dp[j][k] += pre_sum[j][j] - pre_sum[j][i + 1]
                dp[j][k] %= mod

        pre_sum[k][j + 1] = pre_sum[k][j] + dp[j][k]
        pre_sum[k][j + 1] %= mod

ans = sum(dp[i][n] for i in range(n))
ans %= mod
print(ans)
