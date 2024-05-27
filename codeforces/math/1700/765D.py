# -*- coding: utf-8 -*-
# @Time: 2024/4/24 9:29
# @Author: yfwang
# @File: 765D.py

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

n = I()
f = LGMI()

fix_points = []
for i in range(n):
    if f[f[i]] != f[i]:
        exit(print(-1))
    if f[i] == i:
        fix_points.append(i)

m = len(fix_points)
g = [0] * n
h = [0] * m
ind = [0] * n
for i, v in enumerate(fix_points):
    ind[v] = i

for i in range(n):
    g[i] = ind[f[i]]
    if f[i] == i:
        h[g[i]] = i
print(m)
print(' '.join(str(x + 1) for x in g))
print(' '.join(str(x + 1) for x in h))
