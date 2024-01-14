# -*- coding : utf-8 -*-
# @Time: 2024/1/12 19:07
# @Author: yefei.wang
# @File: B.py

import sys

from math import gcd

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
    a, b, c, m = MI()
    x = gcd(a, b)
    x = gcd(x, c)
    ans = True if m % x == 0 else False
    YN(ans)
