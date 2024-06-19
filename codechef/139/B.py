# -*- coding : utf-8 -*-
# @Time: 2024/6/19 22:41
# @Author: yefei.wang
# @File: B.py
import bisect
import sys
from itertools import accumulate


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
                # factors.append(p)
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

N = 10 ** 6 + 5
fact = Factorization(N)
A = []
for x in range(2, N):
    if fact.is_prime(x):
        A.append(x)
PA = list(accumulate(A, initial=0))


tcn = I()
for _tcn_ in range(tcn):
    k = I()
    if fact.is_prime(k):
        i = bisect.bisect_right(A, k)
        ans = PA[i] * k
    else:
        factors = fact.get_factors(k)
        factors.sort()
        i = bisect.bisect_right(A, factors[0])
        ans = PA[i] * k
    print(ans)
