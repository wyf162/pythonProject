# -*- coding: utf-8 -*-
# @Time: 2024/7/19 11:20
# @Author: yfwang
# @File: 1243B2.py

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    s = list(input())
    t = list(input())

    ops = []
    for i in range(n):
        if s[i] == t[i]:
            continue
        if s[i] in s[i + 1:]:
            i1 = s[i + 1:].index(s[i])
            ops.append((i1 + i + 1, i))
            t[i], s[i + i1 + 1] = s[i + i1 + 1], t[i]
        elif t[i] in t[i + 1:]:
            i1 = t[i + 1:].index(t[i])
            ops.append((i, i + i1 + 1))
            s[i], t[i + i1 + 1] = t[i + i1 + 1], s[i]
        elif s[i] in t[i + 1:]:
            i1 = t[i + 1:].index(s[i])
            ops.append((i1 + i + 1, i + i1 + 1))
            t[i + i1 + 1], s[i + i1 + 1] = s[i + i1 + 1], t[i + i1 + 1]
            ops.append((i1 + i + 1, i))
            t[i], s[i + i1 + 1] = s[i + i1 + 1], t[i]
        elif t[i] in s[i + 1:]:
            i1 = s[i + 1:].index(t[i])
            ops.append((i1 + i + 1, i + i1 + 1))
            t[i + i1 + 1], s[i + i1 + 1] = s[i + i1 + 1], t[i + i1 + 1]
            ops.append((i, i + i1 + 1))
            s[i], t[i + i1 + 1] = t[i + i1 + 1], s[i]
        else:
            YN(False)
            break
    else:
        YN(True)
        print(len(ops))
        for i in range(len(ops)):
            print(' '.join(str(x + 1) for x in ops[i]))

    # print(s)
    # print(t)