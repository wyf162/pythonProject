# -*- coding: utf-8 -*-
# @Time: 2024/3/4 15:37
# @Author: yfwang
# @File: 1852A.py
# https://codeforces.com/problemset/problem/1852/A

import bisect
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    if nums[0] != 1:
        print(1)
        continue

    dp = [0] * (k+2)
    dp[1] = 1
    for i in range(2, k+2):
        ok = dp[i-1] + n + 1
        ng = dp[i-1]
        while ok - ng > 1:
            mid = (ok + ng) // 2
            cnt = bisect.bisect_right(nums, mid)
            if mid - cnt >= dp[i-1]:
                ok = mid
            else:
                ng = mid
        dp[i] = ok

    print(dp[k+1])
