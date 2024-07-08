# -*- coding: utf-8 -*-
# @Time: 2024/7/8 9:18
# @Author: yfwang
# @File: 1195D2.py


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
mod = 998244353

tcn = 1
for _tcn_ in range(tcn):
    n = I()
    A = LI()

    cnt = [0] * 11
    for a in A:
        s = list(str(a))
        cnt[len(s)] += 1

    tot = 0
    for a in A:
        s = list(str(a))
        m = len(s)
        for i in range(1, 11):
            s.insert(max(0, m - i + 1), '0')
            x = int(''.join(s))
            tot += x * cnt[i]
            tot %= mod

    for a in A:
        s = list(str(a))
        m = len(s)
        for i in range(1, 11):
            s.insert(max(0, m - i), '0')
            x = int(''.join(s))
            tot += x * cnt[i]
            tot %= mod

    print(tot)
