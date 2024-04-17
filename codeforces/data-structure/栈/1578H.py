# -*- coding: utf-8 -*-
# @Time: 2024/4/17 10:39
# @Author: yfwang
# @File: 1578H.py
# https://codeforces.com/problemset/problem/1578/H

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

s = input().replace('()', '0').replace('->', ',')

nums = []
ops = []

for c in s:
    if c == '0':
        nums.append(0)
    elif c == ',':
        ops.append(1)
    elif c == '(':
        ops.append(0)
    else:
        while ops[-1]:
            x, y = nums.pop(), nums.pop()
            nums.append(max(x, y+1))
            ops.pop()
        ops.pop()
while ops:
    x, y = nums.pop(), nums.pop()
    nums.append(max(x, y + 1))
    ops.pop()

print(nums[0])
