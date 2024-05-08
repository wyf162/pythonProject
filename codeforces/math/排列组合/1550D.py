# -*- coding : utf-8 -*-
# @Time: 2024/5/7 21:33
# @Author: yefei.wang
# @File: 1550D.py
import math
import sys

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

fact = [1]
for i in range(1, 4 * 10 ** 5 + 1):
    fact.append(fact[-1] * i % mod)

fact_inv = [pow(fact[-1], mod - 2, mod)]
for i in range(4 * 10 ** 5, 0, -1):
    fact_inv.append(fact_inv[-1] * i % mod)

fact_inv.reverse()


def comb(a, b):
    if 0 <= b <= a:
        return fact[a] * fact_inv[b] % mod * fact_inv[a - b] % mod
    else:
        return 0


tcn = I()
for _tcn_ in range(tcn):
    n, l, r = MI()
    x, y, z, w = 1 - r, 1 - l, n - r, n - l
    k = min(-x, y, -z, w)
    minus = 0
    plus = 0

    if n % 2 == 0:
        ans = k * comb(n, n // 2) % mod
        for i in range(1, n):
            b = k + i
            if y < b:
                minus += 1
            if z > -b:
                plus += 1
            ans += comb(n - minus - plus, n // 2 - minus)
            ans %= mod
    else:
        ans = k * comb(n, n // 2) * 2 % mod
        for i in range(1, n):
            b = k + i
            if y < b:
                minus += 1
            if z > -b:
                plus += 1
            ans += comb(n - minus - plus, n // 2 - minus)
            ans += comb(n - minus - plus, n // 2 + 1 - minus)
            ans %= mod
    print(ans)
