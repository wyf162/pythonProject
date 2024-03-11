# -*- coding: utf-8 -*-
# @Time: 2024/3/11 9:16
# @Author: yfwang
# @File: 45I.py
# https://codeforces.com/problemset/problem/45/I

import sys
from heapq import heappop, heappush

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
h = []
rst = []
zero = 0
for x in nums:
    if x > 0:
        rst.append(x)
    elif x < 0:
        heappush(h, x)
    else:
        zero += 1
while len(h) >= 2:
    rst.append(heappop(h))
    rst.append(heappop(h))

if rst:
    print(*rst)
else:
    if zero:
        print(0)
    else:
        print(max(h))
