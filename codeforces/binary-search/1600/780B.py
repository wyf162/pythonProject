# -*- coding: utf-8 -*-
# @Time: 2024/6/5 13:59
# @Author: yfwang
# @File: 780B.py
# https://codeforces.com/problemset/problem/780/B

import sys
from math import inf

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
mod2 = 998244353

tcn = 2
for _tcn_ in range(tcn):
    n = I()
    points = LI()
    speeds = LI()


    def check(t):
        left = -inf
        right = inf
        for i in range(n):
            left = max(left, points[i] - speeds[i] * t)
            right = min(right, points[i] + speeds[i] * t)
            if left > right:
                break
        return left <= right


    L = 0
    R = 10 ** 9
    delta = 1e-9
    for _ in range(60):
        # print(L, R)
        mid = (L + R) / 2
        if check(mid):
            ans = mid
            R = mid - delta
        else:
            L = mid + delta
    print(ans)
