# -*- coding : utf-8 -*-
# @Time: 2024/5/11 11:06
# @Author: yefei.wang
# @File: 852F.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())


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


tcn = 1
for _tcn_ in range(tcn):
    N, M, a, Q = MI()

    powers = [1]
    for i in range(10 ** 6 + 124):
        powers.append(powers[-1] * a % Q)
        if powers[-1] == 1:
            powers.pop()
            break

    phi = len(powers)
    fact = Factorial(M, phi)

    ans = [1] * N
    for i in range(N - 2, -1, -1):
        ans[i] = (ans[i + 1] + fact.combi(M, N - 1 - i)) % phi
    print(*[powers[x] for x in ans])
