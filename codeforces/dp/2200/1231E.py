# -*- coding: utf-8 -*-
# @Time: 2024/6/4 17:07
# @Author: yfwang
# @File: 1231E.py

import sys
from collections import Counter

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
    s = input()
    t = input()
    if Counter(s) != Counter(t):
        print(-1)
        continue

    ans = 0
    for i in range(n):
        i1 = i
        j = 0
        while i1 < n and j < n:
            if s[j] == t[i1]:
                i1 += 1
            j += 1
        ans = max(ans, i1-i)

    print(n - ans)
