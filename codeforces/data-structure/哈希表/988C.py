# -*- coding: utf-8 -*-
# @Time: 2024/4/15 9:08
# @Author: yfwang
# @File: 988C.py

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

k = I()
arrs = []
for _ in range(k):
    n = I()
    arrs.append(LI())

hst = dict()
for i, arr in enumerate(arrs):
    tot = sum(arr)
    for j, x in enumerate(arr):
        y = tot - x
        if y in hst and hst[y][0] != i:
            print('YES')
            print(hst[y][0] + 1, hst[y][1] + 1)
            print(i + 1, j + 1)
            exit()
        else:
            hst[y] = (i, j)
print('NO')
