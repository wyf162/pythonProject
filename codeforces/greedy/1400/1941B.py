# -*- coding: utf-8 -*-
# @Time: 2024/3/14 13:35
# @Author: yfwang
# @File: 1941B.py
# https://codeforces.com/contest/1941/problem/B

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    ans = True
    for i in range(n - 2):
        if A[i] < 0:
            ans = False
            break
        A[i + 1] -= 2 * A[i]
        A[i + 2] -= A[i]
        A[i] -= A[i]
    if A[-1] or A[-2]:
        ans = False
    YN(ans)
