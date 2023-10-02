# -*- coding : utf-8 -*-
# @Time: 2023/10/2 13:36
# @Author: yefei.wang
# @File: 1002_flipping-signs.py
import sys
import bisect
sys.stdin = open('./../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
nums = LI()
tot = sum(abs(x) for x in nums)

if 0 not in nums and sum(x < 0 for x in nums) % 2:
    tot -= min(abs(x) for x in nums) * 2
print(tot)
