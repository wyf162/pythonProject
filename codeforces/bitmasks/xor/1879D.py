# -*- coding: utf-8 -*-
# @Time: 2024/2/27 10:34
# @Author: yfwang
# @File: 1879D.py
# https://codeforces.com/problemset/problem/1879/D

import sys
from itertools import accumulate
from operator import xor

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

tcn = I()

for _tcn_ in range(tcn):
    n = I()
    nums = list(accumulate(LI(), func=xor, initial=0))

    ans = 0
    for i in range(30):
        c0, p0 = 0, 0
        c1, p1 = 0, 0
        x = 0
        for idx, v in enumerate(nums):
            if v >> i & 1:
                x += c0 * idx - p0
                c1 += 1
                p1 += idx
            else:
                x += c1 * idx - p1
                c0 += 1
                p0 += idx
        ans += x << i
        ans %= mod2
    print(ans)
