# -*- coding : utf-8 -*-
# @Time: 2024/6/2 20:52
# @Author: yefei.wang
# @File: 803D.py

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
    a = LI()
    c = len(a)
    avg = sum(a) / c
    ulik = math.log(2 * avg + 1) * (-c)
    plik = 0
    for k in a:
        plik += math.log(avg) * k
        plik += -avg
        for i in range(1, k + 1):
            plik -= math.log(i)
    isu = ulik > plik
    ans = ["poisson", "uniform"][isu]
    print(ans)
