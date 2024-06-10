# -*- coding : utf-8 -*-
# @Time: 2024/6/9 22:41
# @Author: yefei.wang
# @File: B.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
    nums = [int(c) for c in input()]
    if len(nums) <= 1:
        YN(False)
        continue
    while nums:
        if len(nums) == 2:
            break
        x = nums.pop()
        if x == 9:
            nums.append(x)
            break

        if nums[-1] >= 1:
            nums[-1] -= 1
        else:
            k = 0
            while nums[-1] == 0:
                k += 1
                nums.pop()
            nums[-1] -= 1
            for i in range(k):
                nums.append(9)
    if nums[0] == 1 and nums[-1] < 9:
        YN(True)
    else:
        YN(False)
