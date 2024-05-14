# -*- coding : utf-8 -*-
# @Time: 2024/5/12 14:14
# @Author: yefei.wang
# @File: 1622D.py
# https://codeforces.com/contest/1622/problem/D


import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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


def comb(a, b):
    if 0 <= b <= a:
        return fact[a] * fact_inv[b] % mod * fact_inv[a - b] % mod
    else:
        return 0


tcn = 3
for _tcn_ in range(tcn):
    n, k = MI()
    A = input()
    i = 0
    cnt = 0
    for j in range(n):
        if A[j] == '1':
            cnt += 1

