# -*- coding: utf-8 -*-
# @Time: 2024/6/20 14:43
# @Author: yfwang
# @File: D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
# sys.stdout = open('../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 0x3f3f3f3f

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    s = ['A'] + list(input())
    A = [0] + LI()
    score = [0] * (n + 1)
    for i in range(1, n + 1):
        score[i] = min(i, A[i] - 1)
    mx = max(score[1:])
    print(mx)

