# -*- coding: utf-8 -*-
# @Time: 2024/4/26 16:44
# @Author: yfwang
# @File: 1499D.py
# https://codeforces.com/contest/1499/problem/D

import sys
import math


class LeastPrimeFactor:

    def __init__(self, n):
        self.N = n
        self.lpf = list(range(self.N + 1))
        self.fc = [1] * (self.N + 1)
        for x in range(2, int(self.N ** .5) + 1):
            if self.lpf[x] == x:
                for y in range(x * x, self.N + 1, x):
                    self.lpf[y] = x
            if self.fc[x] == 1:
                for y in range(x, self.N + 1, x):
                    self.fc[y] <<= 1

    def get_factors(self, x):
        factors = []
        while x > 1:
            p = self.lpf[x]
            x //= p
            factors.append(p)
        return factors

    def get_divisors(self, x):
        factors = []
        while x > 1:
            p = self.lpf[x]
            x //= p
            factors.append(p)
        # print(factors)

        rets = set()
        n = len(factors)
        for i in range((1 << n)):
            x = 1
            for j in range(n):
                if i >> j & 1:
                    x *= factors[j]
            rets.add(x)
        rets = list(sorted(rets))
        return rets


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

lpf = LeastPrimeFactor(20000001)
tcn = I()
for _tcn_ in range(tcn):
    c, d, x = MI()
    # a = A * g
    # b = B * g
    # lcm(a, b) = A * B * g
    # gcd(a, b) = g
    # gcd(A, B) = 1
    # c * lcm(a, b) - d * gcd(a, b) = x
    # c * A * B * g - d * g = x
    divisors = lpf.get_divisors(x)
    ans = 0
    for g in divisors:
        cAB = x // g + d
        if cAB % c:
            continue
        AB = cAB // c
        ans += lpf.fc[AB]
    print(ans)
