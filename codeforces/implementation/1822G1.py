import math
import sys
from collections import Counter
from functools import cache

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7


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

    @cache
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


pf = LeastPrimeFactor(10 ** 6 + 5)

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    rst = 0
    cnt = Counter(a)
    for k, v in cnt.items():
        factors = pf.get_all_factors(k)
        for x in factors[1:]:
            k1, k2 = k // x, k * x
            if k1 in cnt and k2 in cnt:
                rst += cnt[k1] * cnt[k2] * v

        if v >= 3:
            rst += math.comb(v, 3) * 6
    print(rst)
