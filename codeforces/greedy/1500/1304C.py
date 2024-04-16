# -*- coding: utf-8 -*-
# @Time: 2024/4/16 9:05
# @Author: yfwang
# @File: 1304C.py
# https://codeforces.com/problemset/problem/1304/C

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
    n, m = MI()
    customers = [LI() for _ in range(n)]
    cur_ti = 0
    cur_li = m
    cur_hi = m
    ans = True
    for ti, li, hi in customers:
        cur_li = max(li, cur_li - (ti - cur_ti))
        cur_hi = min(hi, cur_hi + (ti - cur_ti))
        cur_ti = ti
        if cur_li > cur_hi:
            ans = False
            break
    YN(ans)
