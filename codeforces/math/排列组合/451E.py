# -*- coding: utf-8 -*-
# @Time: 2024/5/23 8:59
# @Author: yfwang
# @File: 451E.py
# https://codeforces.com/contest/451/problem/E
# 排列组合 容斥原理

import sys
import math

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007


def comb(n, k):
    if n < k:
        return 0
    else:
        return math.comb(n, k) % mod


tcn = 5
for _tcn_ in range(tcn):
    n, s = MI()
    nums = LI()

    ans = 0

    for state in range(1 << n):
        sign = 1 if state.bit_count() % 2 == 0 else -1
        a = s

        for b in range(n):
            if state >> b & 1:
                a -= nums[b] + 1
        tmp = comb(a + n - 1, n - 1)
        ans += tmp * sign
        ans %= mod
    print(ans)
