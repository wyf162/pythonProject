# -*- coding : utf-8 -*-
# @Time: 2024/7/11 23:47
# @Author: yefei.wang
# @File: F.py

import sys


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

    def get_factors(self, n, unique=True):
        factors = []
        while n != 1:
            p = self.sieve[n]
            cnt = 1
            n //= p
            factors.append(p)
            while self.sieve[n] == p:
                cnt += 1
                n //= p
                if unique:
                    continue
                factors.append(p)
        return factors

    def is_prime(self, n):
        return self.sieve[n] == n


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 10 ** 9

fact = Factorization(10 ** 5 + 5)

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    A = LI()
    divs = fact.get_divisors(m)
    divs = set(divs)

    ans = 1
    dp = {1}
    for a in A:
        if a not in divs:
            continue
        ndp = {1, a}
        for x in dp:
            if a * x in divs:
                ndp.add(a * x)
            ndp.add(x)
        if m in ndp:
            ans += 1
            dp = {1, a}
        else:
            dp = ndp
    print(ans)
