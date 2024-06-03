# -*- coding: utf-8 -*-
# @Time: 2024/6/3 9:50
# @Author: yfwang
# @File: 1721D.py
# https://codeforces.com/contest/1721/problem/D
# xor and

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    B = LI()
    ans = 0
    for bit_pos in range(29, -1, -1):
        val = ans | (1 << bit_pos)
        if sorted(a & val for a in A) == sorted(~b & val for b in B):
            ans = val
    print(ans)
