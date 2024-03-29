# -*- coding : utf-8 -*-
# @Time: 2024/1/2 20:58
# @Author: yefei.wang
# @File: 1766D.py

import math
import sys


class LeastPrimeFactor:

    def __init__(self, n):
        self.N = n
        self.lpf = list(range(self.N + 1))
        for x in range(2, int(self.N ** .5) + 1):
            if self.lpf[x] == x:
                for y in range(x * x, self.N + 1, x):
                    self.lpf[y] = x

    def get_factors(self, x):
        factors = []
        while x > 1:
            p = self.lpf[x]
            x //= p
            factors.append(p)
        return factors

    def get_all_factors(self, x):
        factors = []
        while x > 1:
            p = self.lpf[x]
            x //= p
            factors.append(p)
        # print(factors)

        rets = set()
        n = len(factors)
        for i in range((1 << n)):
            x = 1
            for j in range(n):
                if i >> j & 1:
                    x *= factors[j]
            rets.add(x)
        rets = list(sorted(rets))
        return rets


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

lpf = LeastPrimeFactor(10 ** 7 + 5)

tcn = I()
for _tcn_ in range(tcn):
    x, y = MI()
    z = y - x
    if z == 1:
        print(-1)
        continue
    factors = lpf.get_factors(z)
    factors = set(factors)
    ret = y
    for factor in factors:
        z1 = (x + factor - 1) // factor * factor - x
        ret = min(ret, z1)
    print(ret)
