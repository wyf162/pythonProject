# -*- coding: utf-8 -*-
# @Time: 2024/3/15 9:58
# @Author: yfwang
# @File: 1807F.py
# https://codeforces.com/problemset/problem/1807/F

import sys

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
    L = input().split()
    L[0] = int(L[0])
    L[1] = int(L[1])
    L[2] = int(L[2])
    L[3] = int(L[3])
    L[4] = int(L[4])
    L[5] = int(L[5])
    dx = 0
    dy = 0
    m = 0
    if L[6][0] == 'D':
        dx = 1
    else:
        dx = -1
    if L[6][1] == 'L':
        dy = -1
    else:
        dy = 1
    while (L[3] != L[5] or L[2] != L[4]) and L[0] * L[1] > m:
        p = 0
        if 1 > L[2] + dx or L[2] + dx > L[0]:
            dx = dx * -1
            p = 1
        if L[3] + dy > L[1] or 1 > L[3] + dy:
            dy = dy * -1
            p = 1
        m = p + m
        L[2] = dx + L[2]
        L[3] = dy + L[3]
    if L[2] == L[4] and L[3] == L[5]:
        print(m)
    else:
        print(-1)
