# -*- coding : utf-8 -*-
# @Time: 2024/5/24 21:59
# @Author: yefei.wang
# @File: 1512G2.py

import sys

input = sys.stdin.readline


def euclid_sieve(n):
    lp = (n + 1) * [0]
    primes = []
    i = 2
    while i <= n:
        if lp[i] == 0:
            primes.append(i)
            lp[i] = i
        for p in primes:
            if p > lp[i] or i * p > n:
                break
            lp[i * p] = p
        i += 1
    return lp


MAX = int(1e7)
lp = euclid_sieve(MAX)
divsum = (MAX + 1) * [0]
revsum = (MAX + 1) * [-1]
divsum[1] = 1
revsum[1] = 1

for i in range(2, MAX + 1):
    if lp[i] == i:
        divsum[i] = i + 1
    else:
        v = i
        si = 1
        while v % lp[i] == 0:
            v //= lp[i]
            si = si * lp[i] + 1
        divsum[i] = si * divsum[v]

for i in range(MAX, 1, -1):
    if divsum[i] <= MAX:
        revsum[divsum[i]] = i

t = int(input())
print('\n'.join([str(revsum[int(input())]) for _ in range(t)]))
