# -*- coding : utf-8 -*-
# @Time: 2024/1/2 20:11
# @Author: yefei.wang
# @File: 1771C.py

import sys

input = lambda: sys.stdin.readline().rstrip()

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353


def is_prime64(n: int) -> bool:
    st = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}
    if n == 1: return False
    if n == 2: return True
    if n & 1 == 0: return False
    if n in st: return True
    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1
    for a in st:
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1
        if y != n - 1 and t & 1 == 0:
            return False
    return True


def get_primelist(MAX):
    is_prime = [1] * (MAX + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(MAX ** .5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i + i, MAX + 1, i):
            is_prime[j] = 0
    return [i for i, x in enumerate(is_prime) if x]


primes = get_primelist(31623)

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    s = set()
    ans = False
    for x in a:
        if is_prime64(x):
            if x in s:
                ans = True
                break
            s.add(x)
            continue
        for p in primes:
            if p * p > x:
                break
            if x % p == 0:
                if p in s:
                    ans = True
                    break
                s.add(p)
                while x % p == 0:
                    x //= p
        if x != 1:
            if x in s:
                ans = True
                break
            s.add(x)
    if ans:
        print('Yes')
    else:
        print('No')
