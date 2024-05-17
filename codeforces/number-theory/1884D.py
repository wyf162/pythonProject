# -*- coding: utf-8 -*-
# @Time: 2024/5/17 10:17
# @Author: yfwang
# @File: 1884D.py
# 调和级数

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(MI())


class Factorization:

    def __init__(self, n):
        self.N = n + 1
        self.sieve = [-1] * self.N
        for i in range(2, self.N):
            if self.sieve[i] == -1:
                for j in range(i, self.N, i):
                    self.sieve[j] = i

    def get_divisors(self, n):
        divisors = [1]
        while n != 1:
            p = self.sieve[n]
            cnt = 1
            n //= p
            while self.sieve[n] == p:
                cnt += 1
                n //= p
            for i in range(len(divisors)):
                for j in range(1, cnt + 1):
                    divisors.append(divisors[i] * (p ** j))
        return divisors

    def get_factors(self, n):
        factors = []
        while n != 1:
            p = self.sieve[n]
            cnt = 1
            n //= p
            factors.append(p)
            while self.sieve[n] == p:
                cnt += 1
                n //= p
                factors.append(p)
        return factors

    def is_prime(self, n):
        return self.sieve[n] == n


Fact = Factorization(10 ** 6 + 5)

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    if 1 in A:
        print(0)
        continue

    cnt = [0] * (n + 1)
    for a in A:
        cnt[a] += 1
        k = 1
        while a * k <= n:
            cnt[a * k] += 1
            k += 1

    div = [0] * (n + 1)
    for a in A:
        divs = Fact.get_divisors(a)
        for x in divs:
            div[x] += 1

    dp = [0] * (n + 1)
    ans = 0
    for g in range(n, 0, -1):
        dp[g] = (div[g] + 1) * div[g] // 2
        k = 2
        while g * k <= n:
            dp[g] -= dp[g * k]
            k += 1
        if cnt[g] > 0:
            continue
        ans += dp[g]

    print(ans)
