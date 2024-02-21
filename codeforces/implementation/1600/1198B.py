# -*- coding: utf-8 -*-
# @Time: 2024/2/21 9:06
# @Author: yfwang
# @File: 1198B.py
# https://codeforces.com/problemset/problem/1198/B

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
q = I()
events = [LI() for _ in range(q)]
modify = [0] * n
mx = 0
f = [0] * (q + 1)
for i in range(q - 1, -1, -1):
    event = events[i]
    if event[0] == 2:
        f[i] = max(f[i + 1], event[1])
    else:
        f[i] = f[i + 1]

for i, event in enumerate(events):
    if event[0] == 1:
        p, x = event[1] - 1, event[2]
        nums[p] = x
        modify[p] = i

for i in range(n):
    nums[i] = max(nums[i], f[modify[i]])

print(*nums)
