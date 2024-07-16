# -*- coding: utf-8 -*-
# @Time: 2024/7/16 9:05
# @Author: yfwang
# @File: 1891C.py

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
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    nums.sort()
    tot = sum(nums)
    left = 0
    for i, num in enumerate(nums):
        left += num
        right = tot - left
        if left >= right:
            reminder = left - right
            ans = right + n - i - 1 + (reminder + 1) // 2
            if reminder > 1:
                ans += 1
            break
    print(ans)


