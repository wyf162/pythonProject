# -*- coding: utf-8 -*-
# @Time: 2024/5/20 9:08
# @Author: yfwang
# @File: 1354B.py

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
inf = 0x3f3f3f3f

tcn = I()
for _tcn_ in range(tcn):
    s = input()
    n = len(s)
    f1 = [-inf] * (n + 1)
    f2 = [-inf] * (n + 1)
    f3 = [-inf] * (n + 1)
    for i in range(n):
        f1[i + 1] = f1[i]
        f2[i + 1] = f2[i]
        f3[i + 1] = f3[i]
        if s[i] == '1':
            f1[i + 1] = i
        elif s[i] == '2':
            f2[i + 1] = i
        elif s[i] == '3':
            f3[i + 1] = i

    g1 = [inf] * (n + 1)
    g2 = [inf] * (n + 1)
    g3 = [inf] * (n + 1)
    for i in range(n - 1, -1, -1):
        g1[i] = g1[i + 1]
        g2[i] = g2[i + 1]
        g3[i] = g3[i + 1]
        if s[i] == '1':
            g1[i] = i
        elif s[i] == '2':
            g2[i] = i
        elif s[i] == '3':
            g3[i] = i
    ans = inf
    for i in range(n):
        if s[i] == '1':
            tmp = min(g3[i] - f2[i] + 1, g2[i] - f3[i] + 1, i - min(f2[i], f3[i]) + 1, max(g2[i], g3[i]) - i + 1)
            ans = min(ans, tmp)
        elif s[i] == '2':
            tmp = min(g3[i] - f1[i] + 1, g1[i] - f3[i] + 1, i - min(f1[i], f3[i]) + 1, max(g1[i], g3[i]) - i + 1)
            ans = min(ans, tmp)
        elif s[i] == '3':
            tmp = min(g2[i] - f1[i] + 1, g1[i] - f2[i] + 1, i - min(f1[i], f2[i]) + 1, max(g1[i], g2[i]) - i + 1)
            ans = min(ans, tmp)

    if ans <= n:
        print(ans)
    else:
        print(0)
