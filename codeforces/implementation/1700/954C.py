# -*- coding: utf-8 -*-
# @Time: 2024/5/15 9:29
# @Author: yfwang
# @File: 954C.py
# https://codeforces.com/problemset/problem/954/C


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

tcn = 4
for _tcn_ in range(tcn):
    n = I()
    A = LGMI()
    diff = set()
    for i in range(1, n):
        d = A[i] - A[i - 1]
        if d == 0:
            diff = {0, 1}
            break
        elif d in (1, -1):
            continue
        else:
            diff.add(abs(d))
    if len(diff) == 0:
        print('YES')
        print(1, 10**9)
        continue
    elif len(diff) > 1:
        print('NO')
        continue
    y = diff.pop()
    x = 0
    for i in range(n):
        x = max(x, A[i] // y + 1)
    for i in range(1, n):
        pi, pj = A[i - 1] // y, A[i - 1] % y
        ci, cj = A[i] // y, A[i] % y
        # print(pi, pj, ci, cj)
        if pi == ci or pj == cj:
            continue
        else:
            print('NO')
            break
    else:
        print('YES')
        print(x, y)
