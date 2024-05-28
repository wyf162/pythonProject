# -*- coding: utf-8 -*-
# @Time: 2024/5/28 10:27
# @Author: yfwang
# @File: 869C.py

import sys


class Factorial:
    def __init__(self, N, mod) -> None:
        N += 1
        self.mod = mod
        self.f = [1 for _ in range(N)]
        self.g = [1 for _ in range(N)]
        for i in range(1, N):
            self.f[i] = self.f[i - 1] * i % self.mod
        self.g[-1] = pow(self.f[-1], mod - 2, mod)
        for i in range(N - 2, -1, -1):
            self.g[i] = self.g[i + 1] * (i + 1) % self.mod

    def fac(self, n):
        return self.f[n]

    def fac_inv(self, n):
        return self.g[n]

    def combi(self, n, m):
        if n < m or m < 0 or n < 0: return 0
        return self.f[n] * self.g[m] % self.mod * self.g[n - m] % self.mod

    def permu(self, n, m):
        if n < m or m < 0 or n < 0: return 0
        return self.f[n] * self.g[n - m] % self.mod

    def catalan(self, n):
        return (self.combi(2 * n, n) - self.combi(2 * n, n - 1)) % self.mod

    def inv(self, n):
        return self.f[n - 1] * self.g[n] % self.mod


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

fact = Factorial(5005, mod2)

tcn = 4
for _tcn_ in range(tcn):
    a, b, c = MI()
    ans1 = 0
    for k in range(min(a, b) + 1):
        ans1 += fact.fac(k) * fact.combi(a, k) * fact.combi(b, k)

    ans2 = 0
    for k in range(min(a, c) + 1):
        ans2 += fact.fac(k) * fact.combi(a, k) * fact.combi(c, k)

    ans3 = 0
    for k in range(min(c, b) + 1):
        ans3 += fact.fac(k) * fact.combi(c, k) * fact.combi(b, k)

    ans = ans1 * ans2 * ans3 % mod2
    print(ans)
