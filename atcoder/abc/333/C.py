# -*- coding : utf-8 -*-
# @Time: 2023/12/16 20:11
# @Author: yefei.wang
# @File: C.py

import sys

sys.stdin = open('./../../input.txt')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

N = I()

nums = []
k = 0
B = 12
for i in range(B):
    k += pow(10, i)
    nums.append(k)
# print(nums)

a = set()
for i in range(B):
    for j in range(B):
        for k in range(B):
            a.add(nums[i] + nums[j] + nums[k])

b = sorted(a)
# print(len(b))
# print(b[:10])
print(b[N - 1])
# print(len(s))
