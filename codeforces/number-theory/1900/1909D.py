# -*- coding : utf-8 -*-
# @Time: 2024/7/14 15:38
# @Author: yefei.wang
# @File: 1909D.py

import sys
import math

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
    n, x = MI()
    A = LI()
    A = [a - x for a in A]
    A.sort()
    if A[0] == 0 and A[-1] == 0:
        ans = 0
    elif A[0] > 0 or A[-1] < 0:
        A = [abs(a) for a in A[:]]
        g = 0
        for a in A:
            g = math.gcd(g, a)
        ans = sum(a // g for a in A) - n
    else:
        ans = -1
    print(ans)
