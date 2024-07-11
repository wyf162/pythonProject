# -*- coding : utf-8 -*-
# @Time: 2024/7/10 22:45
# @Author: yefei.wang
# @File: B.py

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
mod = 1000000007
mod2 = 998244353
inf = 0x3f3f3f3f


def isPrimeMR(n):
    L = [2, 3, 5, 7, 11, 13, 17]
    if n in L:
        return 1
    d = n - 1
    d = d // (d & -d)
    for a in L:
        t = d
        y = pow(a, t, n)
        if y == 1: continue
        while y != n - 1:
            y = (y * y) % n
            if y == 1 or t == n - 1: return 0
            t <<= 1
    return 1


tcn = I()
for _tcn_ in range(tcn):
    x = I()
    primes = []
    if x == 1:
        x += 1
    while len(primes) < 2:
        if isPrimeMR(x):
            primes.append(x)
        x += 1
    print(primes[0] * primes[1])
