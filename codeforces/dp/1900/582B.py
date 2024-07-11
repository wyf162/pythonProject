# -*- coding: utf-8 -*-
# @Time: 2024/7/11 9:07
# @Author: yfwang
# @File: 582B.py
# LIS

import sys
import bisect
from collections import Counter

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

tcn = 1
for _tcn_ in range(tcn):
    n, t = MI()
    A = LI()
    if t >= n:
        B = A * n
        t -= n
    else:
        B = A * t
        t = 0
    cnt = Counter(A)

    pre = [0] * len(B)
    dp = []
    ans = 1
    for i, b in enumerate(B):
        i1 = bisect.bisect_right(dp, b)
        pre[i] = i1

        if 0 <= i1 < len(dp):
            dp[i1] = b
        else:
            dp.append(b)
    for x in dp:
        ans = max(len(dp) + cnt[x] * t, ans)
    print(ans)

    # post = [0] * len(B)
    # dp = []
    # for i in range(len(B) - 1, -1, -1):
    #     b = -B[i]
    #     i1 = bisect.bisect_left(dp, b)
    #     post[i] = i1
    #     ans = max(i1 + 1 + cnt[b] * t, ans)
    #
    #     if 0 <= i < len(dp):
    #         dp[i] = b
    #     else:
    #         dp.append(b)
