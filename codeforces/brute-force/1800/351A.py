# -*- coding: utf-8 -*-
# @Time: 2024/7/23 9:21
# @Author: yfwang
# @File: 351A.py

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

tcn = 2
for _tcn_ in range(tcn):
    n = I()
    A = [int(s.replace('.', '')[-3:]) for s in input().split(' ')]

    ans = n * 2000
    tot = sum(A)
    m = A.count(0)
    for i in range(m+1):
        ans = min(ans, abs((n-i)*1000-tot))

    ans = ans / 1000
    print("%.3f" % ans)
