# -*- coding : utf-8 -*-
# @Time: 2024/4/29 22:58
# @Author: yefei.wang
# @File: C.py

import sys
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
    dp = [[inf] * (k + 1) for _ in range(n)]
    for i in range(n):
        for j in range(k + 1):
            for l in range(j + 1):
                if l >= i:
                    mn = inf
                    for c in range(i + 1):
                        mn = min(mn, nums[c])
                    dp[i][j] = min(dp[i][j], mn * (i + 1))
                else:
                    mn = inf
                    for c in range(i - l, i + 1):
                        mn = min(mn, nums[c])
                    dp[i][j] = min(dp[i][j], dp[i - l - 1][j - l] + mn * (l + 1))
    print(dp[-1][k])
