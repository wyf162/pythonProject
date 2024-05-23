# -*- coding: utf-8 -*-
# @Time: 2024/5/23 11:17
# @Author: yfwang
# @File: 900C.py
# https://codeforces.com/problemset/problem/900/C
# permutation

import sys

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

tcn = 1
for _tcn_ in range(tcn):
    n = I()
    nums = LGMI()
    cnt = [0] * n

    mx1, mx2 = -1, -1
    for x in nums:
        if x > mx1:
            cnt[x] -= 1
            mx1, mx2 = x, mx1
        elif x > mx2:
            cnt[mx1] += 1
            mx2 = x
    ans = cnt.index(max(cnt)) + 1
    print(ans)
