# -*- coding: utf-8 -*-
# @Time: 2024/4/2 9:18
# @Author: yfwang
# @File: 1299A.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
nums = LI()

for b in range(30, -1, -1):
    one = 0
    idx = -1
    for i in range(n):
        if (nums[i] >> b) & 1:
            one += 1
            idx = i
    if one == 1:
        nums.insert(0, nums.pop(idx))
        break
print(*nums)
