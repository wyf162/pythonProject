# -*- coding : utf-8 -*-
# @Time: 2024/4/29 22:58
# @Author: yefei.wang
# @File: C.py

import sys
from itertools import accumulate
from math import inf

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

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    nums = LI()
    pre_sum = list(accumulate(nums, initial=0))
    dp = [[[inf for _ in range(k + 1)] for _ in range(k + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 0
    dp[1][0][0] = nums[0]
    for i in range(1, n):
        for k1 in range(k + 1):
            for k2 in range(min(i, k + 1)):
                if k2 > k1:
                    continue
                dp[i + 1][k1][k2] = min(dp[i + 1][k1][k2], dp[i][k1][k2] + nums[i])
                if k1 == k or k2 == k:
                    continue
                dp[i + 1][k1 + 1][k2 + 1] = min(dp[i + 1][k1 + 1][k2 + 1],
                                                dp[i - k2 - 1][k1 - k2][0] + min(nums[i - k2 - 1:i + 1]) * (k2 + 2))

    ans = min(min(dp[n][i]) for i in range(k + 1))
    print(ans)
