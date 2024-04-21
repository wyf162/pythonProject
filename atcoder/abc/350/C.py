# -*- coding : utf-8 -*-
# @Time: 2024/4/20 20:13
# @Author: yefei.wang
# @File: C.py

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
nums = LGMI()
ind = [0] * n
for i, x in enumerate(nums):
    ind[x] = i

ops = []
for i in range(n):
    if nums[i] == i:
        continue
    j = ind[i]
    ops.append((i, j))
    ind[i] = i
    ind[nums[i]] = j
    nums[j] = nums[i]
    nums[i] = i
print(len(ops))
for i in range(len(ops)):
    print(ops[i][0] + 1, ops[i][1] + 1)
