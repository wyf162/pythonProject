# -*- coding : utf-8 -*-
# @Time: 2024/5/1 11:26
# @Author: yefei.wang
# @File: 1777C.py
# https://codeforces.com/problemset/problem/1777/C

import sys
from collections import Counter


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


fact = Factorization(10 ** 5 + 5)
input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    A = LI()
    A = list(set(A))
    if m == 1:
        print(0)
        continue
    st = set()
    A.sort()
    nums = []
    for a in A:
        divs = fact.get_divisors(a)
        for div in divs:
            if 1 <= div <= m:
                nums.append((a, div))
                st.add(div)
    if len(st) < m:
        print(-1)
        continue
    # print(nums)

    ans = 10 ** 5 + 5
    cnt = 0
    hst = Counter()
    i = 0
    for j in range(len(nums)):
        div = nums[j][1]
        hst[div] += 1
        if hst[div] == 1:
            cnt += 1
        while cnt == m:
            ans = min(ans, nums[j][0] - nums[i][0])
            div = nums[i][1]
            if hst[div] > 1:
                hst[div] -= 1
                i += 1
            else:
                break
    print(ans)
