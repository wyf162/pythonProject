# -*- coding: utf-8 -*-
# @Time: 2024/2/27 9:20
# @Author: yfwang
# @File: 1541B.py
# https://codeforces.com/problemset/problem/1541/B

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
    n = I()
    nums = LI()
    nums = [(x, i) for i, x in enumerate(nums, start=1)]
    nums.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if nums[i][0] * nums[j][0] >= 2 * n:
                break
            if nums[i][0] * nums[j][0] ==  nums[i][1] + nums[j][1]:
                ans += 1
    print(ans)
