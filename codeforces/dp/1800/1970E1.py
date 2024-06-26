# -*- coding: utf-8 -*-
# @Time: 2024/6/26 13:40
# @Author: yfwang
# @File: 1970E1.py

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

m, n = MI()
A = LI()
B = LI()

f = [[0 for _ in range(m)] for _ in range(n + 1)]
f[0][0] = 1
for i in range(n):
    for j1 in range(m):
        for j2 in range(m):
            f[i + 1][j2] += f[i][j1] * (A[j1] * A[j2] + A[j1] * B[j2] + B[j1] * A[j2])
            f[i + 1][j2] %= mod
ans = sum(f[n])
print(ans)
