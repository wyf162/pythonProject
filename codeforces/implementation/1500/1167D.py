# -*- coding: utf-8 -*-
# @Time: 2024/7/18 15:03
# @Author: yfwang
# @File: 1167D.py

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
inf = 10 ** 6

tcn = 2
for _tcn_ in range(tcn):
    n = I()
    rbs = input()
    stk = []
    mx = 0
    color = [0] * n
    for i, c in enumerate(rbs):
        if c == '(':
            if stk:
                color[i] = color[stk[-1]] ^ 1
            stk.append(i)
            mx = max(mx, len(stk))
        else:
            color[i] = color[stk.pop()]

    print(''.join(str(x) for x in color))

    rbs1 = []
    rbs0 = []
    for i in range(n):
        if color[i] == 0:
            rbs0.append(rbs[i])
        elif color[i] == 1:
            rbs1.append(rbs[i])

    print(rbs0)
    print(rbs1)