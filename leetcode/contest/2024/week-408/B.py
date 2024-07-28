# -*- coding : utf-8 -*-
# @Time: 2024/7/28 10:32
# @Author: yefei.wang
# @File: B.py
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


N = 10 ** 5
fact = Factorization(N)
A = []
for x in range(2, N):
    if fact.is_prime(x):
        A.append(x * x)

# print(A[:10])


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        i1 = bisect.bisect_left(A, l)
        i2 = bisect.bisect_right(A, r)
        # print(i1, i2)
        ans = (r - l + 1) - (i2 - i1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    l = 1
    r = 4
    ret = sol.nonSpecialCount(l, r)
    print(ret)
