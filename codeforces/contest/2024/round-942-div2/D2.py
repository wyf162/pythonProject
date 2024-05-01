# -*- coding : utf-8 -*-
# @Time: 2024/5/1 0:44
# @Author: yefei.wang
# @File: D2.py

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


import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

N = 2 * 10 ** 6 + 5
fact = Factorization(N)

tcn = I()
for _tcn_ in range(tcn):
    a, b = MI()
    ans = 0
    st = set()
    for i in range(2, b + 1):
        divs = fact.get_divisors(i)
        for div in divs:
            if 0 < div - 1 <= a // i:
                st.add((i * (div - 1), i))

    for i in range(2, a + 1):
        divs = fact.get_divisors(i)
        for div in divs:
            if 0 < div - 1 <= b // i:
                st.add((i, i * (div - 1)))
    print(len(st))
