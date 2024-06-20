# -*- coding: utf-8 -*-
# @Time: 2024/6/20 9:11
# @Author: yfwang
# @File: 1926G.py
# trees

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
inf = 10 ** 8

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    parent = [-1] + LGMI()
    s = input()

    f = [[0, 0] for _ in range(n)]
    for y in range(n-1, -1, -1):
        if s[y] == 'P':
            f[y][0] = inf
        elif s[y] == 'S':
            f[y][1] = inf
        x = parent[y]
        if x == -1:
            continue
        f[x][0] += min(f[y][0], f[y][1] + 1)
        f[x][1] += min(f[y][1], f[y][0] + 1)

    print(min(f[0][0], f[0][1]))


