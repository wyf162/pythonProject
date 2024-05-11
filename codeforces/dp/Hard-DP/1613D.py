# -*- coding : utf-8 -*-
# @Time: 2024/5/11 19:24
# @Author: yefei.wang
# @File: 1613D.py
# https://codeforces.com/contest/1613/problem/D
# mex

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
mod = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    dp0 = [0] * (n + 3)
    dp1 = [0] * (n + 3)
    for i, num in enumerate(nums):
        if num > n:
            continue
        dp0[num] += dp0[num]
        dp1[num] += dp1[num]
        if num >= 1:
            dp0[num] += dp0[num - 1]
        if num >= 2:
            dp1[num] += dp0[num - 2]
        dp1[num + 2] += dp1[num + 2]
        if num == 0:
            dp0[0] += 1
        if num == 1:
            dp1[1] += 1
        dp0[num] %= mod
        dp1[num] %= mod
    # print(dp0)
    # print(dp1)
    ans = sum(dp0) + sum(dp1)
    ans %= mod
    print(ans)
