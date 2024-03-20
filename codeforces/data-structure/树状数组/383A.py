# -*- coding: utf-8 -*-
# @Time: 2024/3/20 10:14
# @Author: yfwang
# @File: 383A.py
# https://codeforces.com/problemset/problem/383/A

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

ans = 0
one = 0
for i in range(n):
    if nums[i] == 0:
        ans += one
    else:
        one += 1
print(ans)
