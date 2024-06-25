# -*- coding: utf-8 -*-
# @Time: 2024/6/25 9:07
# @Author: yfwang
# @File: 1883F.py

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

from collections import Counter

tcn = I()
for _tcn_ in range(tcn):
    N = I()
    A = LI()
    C = Counter(A)
    D = {}
    ans = 0
    for a in A:
        D[a] = 1
        C[a] -= 1
        if C[a] == 0:
            ans += len(D)
    print(ans)
