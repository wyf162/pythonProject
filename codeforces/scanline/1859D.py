# -*- coding: utf-8 -*-
# @Time: 2024/2/28 13:13
# @Author: yfwang
# @File: 1859D.py
# https://codeforces.com/problemset/problem/1859/D


import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    n = I()
    segments = [LI() for _ in range(n)]
    q = I()
    X = LI()
    segments += [[x] * 4 for x in X]

    segments.sort(key=lambda x: -x[3])
    qans = {b: b for l, r, a, b in segments}
    j = 0
    for l, r, a, b in segments:
        while b < segments[j][0]:
            j += 1
        qans[b] = qans[segments[j][3]]
    print(*[qans[x] for x in X])
