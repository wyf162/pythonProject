# -*- coding : utf-8 -*-
# @Time: 2024/5/26 14:18
# @Author: yefei.wang
# @File: 258C.py
import bisect


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

tcn = 1
for _tcn_ in range(tcn):
    n = I()
    nums = LI()

    m = max(nums)
    counts = [0] * (m + 1)
    for num in nums:
        counts[num] += 1

    for i in range(m, 0, -1):
        counts[i - 1] += counts[i]

    factors = [[] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(i, m + 1, i):
            factors[j].append(i)

    ans = 0

    for i in range(1, m + 1):
        res = 1
        k = len(factors[i])
        for j in range(1, k):
            res = res * pow(j, counts[factors[i][j - 1]] - counts[factors[i][j]], mod) % mod
        res = res * (pow(k, counts[i], mod) - pow(k - 1, counts[i], mod)) % mod
        ans += res
    print(ans % mod)
