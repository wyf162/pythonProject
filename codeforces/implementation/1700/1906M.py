# -*- coding: utf-8 -*-
# @Time: 2024/2/23 10:45
# @Author: yfwang
# @File: 1906M.py
# https://codeforces.com/problemset/problem/1906/M

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
A = LI()
mx = max(A)
s = sum(A)

if mx > 2 * (s - mx):
    print(s - mx)
else:
    print(s // 3)
