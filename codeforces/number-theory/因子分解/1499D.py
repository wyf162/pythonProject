# -*- coding: utf-8 -*-
# @Time: 2024/4/26 16:44
# @Author: yfwang
# @File: 1499D.py
# https://codeforces.com/contest/1499/problem/D

import sys

from sys import stdin

input = lambda: stdin.readline()[:-1]


class Factorization:

    def __init__(self, n):
        self.N = n + 1
        self.sieve = [-1] * self.N
        self.fc = [1] * self.N
        for i in range(2, self.N):
            if self.sieve[i] == -1:
                for j in range(i, self.N, i):
                    self.sieve[j] = i
                    self.fc[j] <<= 1

    def get_divisors(self, n):
        divisors = [1]
        while n != 1:
            p = self.sieve[n]
            cnt = 1
            n //= p
            while self.sieve[n] == p:
                cnt += 1
                n //= p
            s = divisors.copy()
            for i in s:
                for j in range(1, cnt + 1):
                    divisors.append(i * (p ** j))
        return divisors

    def get_factors(self, n):
        factors = [1]
        while n != 1:
            p = self.sieve[n]
            cnt = 1
            n //= p
            while self.sieve[n] == p:
                cnt += 1
                n //= p
                factors.append(p)
        return factors


sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

fact = Factorization(20000001)
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
    divisors = fact.get_divisors(x)
    ans = 0
    for g in divisors:
        cAB = x // g + d
        if cAB % c:
            continue
        AB = cAB // c
        ans += fact.fc[AB]
    print(ans)
