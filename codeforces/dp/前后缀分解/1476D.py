# -*- coding: utf-8 -*-
# @Time: 2024/4/18 16:46
# @Author: yfwang
# @File: 1476D.py
# https://codeforces.com/contest/1476/problem/D

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


def pp(s):
    print(0, end='')
    for i in range(n):
        if s[i] == 'L':
            print('<-', end='')
        else:
            print('->', end='')
        print(i + 1, end='')
    print()


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    s = list(input())
    rets = [0] * (n + 1)

    f0 = [0] * (n + 1)
    f1 = [0] * (n + 1)
    for i in range(n):
        if s[i] == 'L':
            f0[i + 1] = f1[i] + 1
        else:
            f1[i + 1] = f0[i] + 1

    g0 = [0] * (n + 1)
    g1 = [0] * (n + 1)
    for i in range(n):
        if s[n - i - 1] == 'L':
            g0[i + 1] = g1[i] + 1
        else:
            g1[i + 1] = g0[i] + 1

    for i in range(n + 1):
        x1 = f0[i]
        x2 = g1[n - i]

        rets[i] = x1 + x2 + 1
    print(*rets)
    # for i in range(n + 1):
    #     x1 = 0
    #     for j in range(i - 1, -1, -1):
    #         if x1 % 2 == 0 and s[j] == 'L':
    #             x1 += 1
    #         elif x1 % 2 == 1 and s[j] == 'R':
    #             x1 += 1
    #         else:
    #             break
    #     x2 = 0
    #     for j in range(i, n, 1):
    #         if x2 % 2 == 0 and s[j] == 'R':
    #             x2 += 1
    #         elif x2 % 2 == 1 and s[j] == 'L':
    #             x2 += 1
    #         else:
    #             break
    #     rets[i] = x1 + x2 + 1
    # print(*rets)
