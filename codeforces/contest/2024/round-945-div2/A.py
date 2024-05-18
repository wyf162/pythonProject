# -*- coding : utf-8 -*-
# @Time: 2024/5/17 22:34
# @Author: yefei.wang
# @File: A.py

import sys

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
    nums = LI()
    tot = sum(nums)
    if tot % 2:
        print(-1)
        continue
    nums.sort()
    if nums[0] + nums[1] >= nums[2]:
        print(tot // 2)
    else:
        print(sum(nums[:2]))
