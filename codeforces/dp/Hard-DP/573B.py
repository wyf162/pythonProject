# -*- coding : utf-8 -*-
# @Time: 2024/4/27 14:47
# @Author: yefei.wang
# @File: 573B.py
# https://codeforces.com/problemset/problem/573/B

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

nums[0] = nums[-1] = 1
for i in range(1, n):
    nums[i] = min(nums[i], nums[i - 1] + 1)

for i in range(n - 2, -1, -1):
    nums[i] = min(nums[i], nums[i + 1] + 1)

print(max(nums))
