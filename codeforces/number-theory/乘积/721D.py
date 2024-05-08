# -*- coding: utf-8 -*-
# @Time: 2024/5/8 9:37
# @Author: yfwang
# @File: 721D.py

import sys
from heapq import heappop, heappush, heapify

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

n, k, x = MI()
nums = LI()

neg = False
for num in nums:
    if num < 0:
        neg = not neg

if not neg:
    idx = 0
    for i in range(n):
        if abs(nums[i]) < abs(nums[idx]):
            idx = i

    ops = (abs(nums[idx]) - 1) // x + 1

    if k >= ops:
        if nums[idx] < 0: neg = not neg
        k -= ops
        nums[idx] += ops * x if nums[idx] < 0 else -ops * x
    else:
        nums[idx] += k * x if nums[idx] < 0 else -k * x
        print(' '.join(map(str, nums)))
        exit()

# 相当于把 (abs(nums[i]), i) 作为一个数对放入堆中
hpq = [abs(nums[i]) * n + i for i in range(n)]
heapify(hpq)

for _ in range(k):
    i = heappop(hpq) % n
    if nums[i] == 0 and not neg:
        nums[i] = -x
        neg = True
    else:
        nums[i] += x if nums[i] >= 0 else -x
    heappush(hpq, abs(nums[i]) * n + i)

print(' '.join(map(str, nums)))
