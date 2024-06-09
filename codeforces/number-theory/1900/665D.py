# -*- coding : utf-8 -*-
# @Time: 2024/6/9 10:11
# @Author: yefei.wang
# @File: 665D.py

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

fact = Factorization(2 * 10 ** 6 + 5)
tcn = 4
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    one = nums.count(1)
    if one >= 2:
        for x in nums:
            if x != 1 and fact.is_prime(x + 1):
                print(one + 1)
                rets = [x] + [1] * one
                print(*rets)
                break
        else:
            print(one)
            rets = [1] * one
            print(*rets)
    else:
        ans = False
        for i in range(n):
            for j in range(i + 1, n):
                if fact.is_prime(nums[i] + nums[j]):
                    print(2)
                    print(nums[i], nums[j])
                    ans = True
                    break
            if ans:
                break

        if ans is False:
            print(1)
            print(nums[0])
