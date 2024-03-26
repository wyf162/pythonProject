# -*- coding: utf-8 -*-
# @Time: 2024/3/26 9:12
# @Author: yfwang
# @File: 166C.py
# https://codeforces.com/problemset/problem/166/C

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

n, x = MI()
nums = LI()
ans = 0
if x not in nums:
    nums.append(x)
    ans += 1

nums.sort()
i1 = n
i2 = -1
for i, v in enumerate(nums):
    if v == x:
        i1 = i
        break

for i, v in enumerate(nums):
    if v == x:
        i2 = i

mid = (len(nums) - 1) // 2
if i1 <= mid <= i2:
    pass
elif mid < i1:
    ans += i1 * 2 - len(nums) + 1
elif mid > i2:
    ans += len(nums) - i2 * 2 - 2
print(ans)
