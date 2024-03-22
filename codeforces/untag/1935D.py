# -*- coding: utf-8 -*-
# @Time: 2024/3/22 17:13
# @Author: yfwang
# @File: 1935D.py
# https://codeforces.com/problemset/problem/1935/D

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, c = MI()
    nums = LI()
    ans = (c + 1) * (c+2) // 2
    even = odd = 0
    for i in range(n):
        ans -= nums[i] // 2 + 1
        ans -= c - nums[i] + 1
        if nums[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    ans += even * (even + 1) // 2
    ans += odd * (odd + 1) // 2
    print(ans)
