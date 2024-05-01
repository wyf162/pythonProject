# -*- coding : utf-8 -*-
# @Time: 2024/4/26 22:35
# @Author: yefei.wang
# @File: factorization.py

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


if __name__ == '__main__':
    fact = Factorization(1000000)
    print(fact.get_factors(720720))
    print(fact.get_factors(720720).__len__())
    print(fact.get_divisors(720720))
    print(fact.get_divisors(720720).__len__())
    print(fact.is_prime(100003))

    N = 60060
    print(fact.get_factors(N))
    print(fact.get_factors(N).__len__())
    print(fact.get_divisors(N))
    print(fact.get_divisors(N).__len__())