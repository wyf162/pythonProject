# -*- coding: utf-8 -*-
# @Time: 2024/6/4 13:52
# @Author: yfwang
# @File: 1025B.py
# https://codeforces.com/problemset/problem/1025/B

import math
import sys
from random import shuffle

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

tcn = 3
for _tcn_ in range(tcn):
    n = I()
    pairs = [LI() for _ in range(n)]
    shuffle(pairs)
    factors = set()
    x1, x2 = pairs[0]
    for i in range(1, int(math.sqrt(x1)) + 1):
        if x1 % i == 0:
            factors.add(i)
            factors.add(x1 // i)
    for i in range(1, int(math.sqrt(x2)) + 1):
        if x2 % i == 0:
            factors.add(i)
            factors.add(x2 // i)
    factors.remove(1)
    factors = list(sorted(factors))
    unfit = set()
    ans = -1
    for factor in factors:
        if any(factor % x == 0 for x in unfit):
            continue
        ans = factor
        for i in range(1, n):
            if pairs[i][0] % factor == 0 or pairs[i][1] % factor == 0:
                continue
            else:
                ans = -1
                break
        if ans > 0:
            break
        else:
            unfit.add(factor)
    print(ans)
