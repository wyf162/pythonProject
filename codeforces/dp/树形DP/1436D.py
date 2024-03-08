# -*- coding: utf-8 -*-
# @Time: 2024/3/8 9:50
# @Author: yfwang
# @File: 1436D.py
# https://codeforces.com/contest/1436/problem/D


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
fa = [-1] + LGMI()
nums = LI()

dp = nums[:]
size = [0] * n
for i in range(n-1, 0, -1):
    if size[i] == 0:
        size[i] = 1
    dp[fa[i]] += dp[i]
    size[fa[i]] += size[i]

print(max((a-1) // b + 1 for a, b in zip(dp, size)))
