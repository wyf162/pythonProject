# -*- coding : utf-8 -*-
# @Time: 2024/6/15 20:37
# @Author: yefei.wang
# @File: E.py


import os
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


# 请在此输入您的代码
sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, k = MI()
A = LI()
PA = list(accumulate(A, initial=0))

mx = max(A)
vis = [0] * (mx + 1)
fact = Factorization(mx + 5)
ans = PA[-1]

for g in range(mx, 0, -1):
    i = j = 0
    while j < n:
        if A[j] % g == 0:
            j += 1
        else:
            if j - i + 1 > k:
                ans = max(ans, (PA[j] - PA[i]) * g)
            j += 1
            i = j


print(ans)
