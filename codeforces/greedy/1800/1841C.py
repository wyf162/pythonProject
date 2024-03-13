# -*- coding: utf-8 -*-
# @Time: 2024/3/13 17:08
# @Author: yfwang
# @File: 1841C.py

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

c2v = {'A': 1, 'B': 10, 'C': 100, 'D': 1000, 'E': 10000}


def computer(nums):
    n = len(nums)
    val = 0
    mx = 0
    for i in range(n - 1, -1, -1):
        if nums[i] < mx:
            val -= nums[i]
        else:
            val += nums[i]
            mx = max(mx, nums[i])
    return val


tcn = I()
for _tcn_ in range(tcn):
    s = input()
    nums = [c2v[c] for c in s]
    n = len(nums)
    ans = []

    rnums = list(reversed(nums))

    for v1 in c2v.values():
        if v1 in nums:
            i = n - 1 - rnums.index(v1)
            for v2 in c2v.values():
                nums[i] = v2
                t = computer(nums)
                ans.append(t)
            nums[i] = v1

    for v1 in c2v.values():
        if v1 in nums:
            i = nums.index(v1)
            for v2 in c2v.values():
                nums[i] = v2
                t = computer(nums)
                ans.append(t)
            nums[i] = v1

    ret = max(ans)
    print(ret)
