# -*- coding : utf-8 -*-
# @Time: 2023/10/4 13:17
# @Author: yefei.wang
# @File: 1004.py

import sys

sys.stdin = open('./../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, k = MI()
a = LI()

pre_sum = [0] * (n + 1)
for i in range(n):
    pre_sum[i + 1] = pre_sum[i] + a[i]

nums = []
for i in range(n):
    for j in range(i + 1):
        nums.append(pre_sum[i + 1] - pre_sum[j])

nums.sort()
# print(nums)

B = len(bin(nums[-1])[2:])
ans = 0
for b in range(B, -1, -1):
    vis = []
    for i, num in enumerate(nums):
        if num >> b & 1:
            vis.append(i)
    if len(vis) >= k:
        ans |= (1 << b)
        j = 0
        for i in vis:
            nums[j] = nums[i]
            j += 1
        nums = nums[:len(vis)]
print(ans)
