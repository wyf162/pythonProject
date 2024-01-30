# -*- coding : utf-8 -*-
# @Time: 2024/1/29 20:54
# @Author: yefei.wang
# @File: 1452D.py

import math

modm = 998244353


def facstpow(a, b):
    if b == 0:
        return 1
    else:
        t = facstpow(a, b // 2)
        if b % 2 == 1:
            return (((t * t) % modm) * a) % modm
        return (t * t) % modm


def inver(a):
    return facstpow(a, modm - 2)


fact = [1 for i in range(2 * (10 ** 5) + 2)]
for i in range(1, 2 * (10 ** 5) + 2):
    fact[i] = (fact[i - 1] * i) % modm


def bin(n, k):
    return ((fact[n]) * (inver(fact[k]) * inver(fact[n - k])) % modm) % modm


n = int(input())
ans = 0
for t in range(1, n + 1):
    if (t - n) % 2 == 0:
        ner = (t + n) // 2
        if ner >= t:
            ans += bin(ner - 1, t - 1)
            ans %= modm
print((ans * inver(facstpow(2, n))) % modm)
