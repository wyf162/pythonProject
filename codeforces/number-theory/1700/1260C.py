# -*- coding : utf-8 -*-
# @Time: 2024/5/23 20:47
# @Author: yefei.wang
# @File: 1260C.py
# https://codeforces.com/problemset/problem/1260/C
# 裴蜀定理

import math
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
    r, b, k = MI()
    if r > b:
        r, b = b, r
    g = math.gcd(r, b)
    r = r // g
    b = b // g

    if b > r * (k - 1) + 1:
        print('rebel')
    else:
        print('obey')
