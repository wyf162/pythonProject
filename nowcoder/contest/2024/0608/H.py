# -*- coding : utf-8 -*-
# @Time: 2024/6/8 14:50
# @Author: yefei.wang
# @File: H.py
# perm mex

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
    n = I()
    nums = LI()
    if nums[-1] != n:
        print(0)
        continue
    cnt = 1
    for i in range(1, n):
        if nums[i - 1] > nums[i]:
            cnt = 0
            break
        elif nums[i - 1] == nums[i]:
            cnt *= (i + 1 - nums[i - 1])
            cnt %= mod2
    print(cnt)
