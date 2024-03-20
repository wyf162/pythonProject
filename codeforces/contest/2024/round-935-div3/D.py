# -*- coding: utf-8 -*-
# @Time: 2024/3/19 17:08
# @Author: yfwang
# @File: D.py

import sys

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
    n, m = MI()
    A = LI()
    B = LI()
    tot = 0
    for i in range(n - 1, m - 1, -1):
        tot += min(A[i], B[i])

    ans = 1 << 64
    for i in range(m - 1, -1, -1):
        ans = min(ans, tot + A[i])
        tot += min(A[i], B[i])
    print(ans)
