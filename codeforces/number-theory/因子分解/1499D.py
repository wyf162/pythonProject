# -*- coding: utf-8 -*-
# @Time: 2024/4/26 16:44
# @Author: yfwang
# @File: 1499D.py
# https://codeforces.com/contest/1499/problem/D

import sys

N = 20000001
sieve = [-1] * N
fc = [1] * N
for i in range(2, N):
    if sieve[i] == -1:
        for j in range(i, N, i):
            sieve[j] = i
            fc[j] <<= 1


def get_divisors(n):
    divisors = [1]
    while n != 1:
        p = sieve[n]
        cnt = 1
        n //= p
        while sieve[n] == p:
            cnt += 1
            n //= p
        for i in range(len(divisors)):
            for j in range(1, cnt + 1):
                divisors.append(divisors[i] * (p ** j))
    return divisors


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
    c, d, x = MI()
    # a = A * g
    # b = B * g
    # lcm(a, b) = A * B * g
    # gcd(a, b) = g
    # gcd(A, B) = 1
    # c * lcm(a, b) - d * gcd(a, b) = x
    # c * A * B * g - d * g = x
    divisors = get_divisors(x)
    ans = 0
    for g in divisors:
        cAB = x // g + d
        if cAB % c:
            continue
        AB = cAB // c
        ans += fc[AB]
    print(ans)
