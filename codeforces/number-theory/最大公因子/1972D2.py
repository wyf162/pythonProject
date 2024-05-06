# -*- coding : utf-8 -*-
# @Time: 2024/5/6 21:59
# @Author: yefei.wang
# @File: 1972D2.py

import sys
import math

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
    ans = 0
    for a in range(1, math.isqrt(n) + 1):
        for b in range(1, math.isqrt(m) + 1):
            if math.gcd(a, b) == 1:
                ans += min(n // a // (a + b), m // b // (a + b))
    print(ans)
