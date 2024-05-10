# -*- coding: utf-8 -*-
# @Time: 2024/5/10 14:25
# @Author: yfwang
# @File: 1569C.py

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
mod = 998244353

N = 2 * 10 ** 5
fact = [1]
for i in range(1, N + 1):
    fact.append(fact[-1] * i % mod)

fact_inv = [pow(fact[-1], mod - 2, mod)]
for i in range(N, 0, -1):
    fact_inv.append(fact_inv[-1] * i % mod)

fact_inv.reverse()

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    A.sort()
    if A[-1] - A[-2] == 0:
        ans = fact[n]
    elif A[-1] - A[-2] == 1:
        x = A.count(A[-2])
        ans = fact[n] * fact_inv[x+1] * (fact[x+1] - fact[x]) % mod
    else:
        ans = 0
    print(ans)
