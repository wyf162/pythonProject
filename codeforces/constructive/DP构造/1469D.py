# -*- coding: utf-8 -*-
# @Time: 2024/4/17 13:26
# @Author: yfwang
# @File: 1469D.py
# https://codeforces.com/contest/1469/problem/D

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


def cd(x, y):
    return (x + y - 1) // y


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    out = []
    large = n
    for i in range(n - 1, 1, -1):
        while cd(large, i) in [i, i + 1]:
            out.append([n, i])
            large = cd(large, i)
        out.append([i, n])
    print(len(out))
    for i in range(len(out)):
        print(*out[i])


def solve2():
    n = int(input())
    ops = []
    beeg = n
    for i in range(n - 1, 1, -1):
        if (i - 1) ** 2 < beeg:
            ops.append((beeg, i))
            ops.append((beeg, i))
            beeg = i
        else:
            ops.append((i, beeg))
    print(len(ops))
    for op in ops:
        print(*op)
