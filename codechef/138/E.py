# -*- coding : utf-8 -*-
# @Time: 2024/6/12 22:59
# @Author: yefei.wang
# @File: E.py

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

N = 10 ** 5 + 10
fact = Factorization(N)
st = set()
primes = []
for x in range(3, N):
    if fact.is_prime(x):
        primes.append(x)
        st.add(x * x)

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    n -= 4
    ans = False
    for x in primes:
        y = n - x * x
        if y <= 0:
            break
        if y in st and y != x * x:
            ans = True
            break
    YN(ans)
