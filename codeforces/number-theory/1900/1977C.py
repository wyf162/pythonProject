# -*- coding: utf-8 -*-
# @Time: 2024/5/27 9:26
# @Author: yfwang
# @File: 1977C.py
# https://codeforces.com/contest/1977/problem/C
# lcm divisor

import sys
from math import lcm

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


def divisors(M):
    d = []
    i = 1
    while M >= i ** 2:
        if M % i == 0:
            d.append(i)
            if i ** 2 != M:
                d.append(M // i)
        i = i + 1
    return d


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    st = set(nums)

    L = 1
    for x in nums:
        L = lcm(L, x)
    if L not in st:
        print(n)
        continue

    ans = 0
    divs = divisors(L)
    for d in divs:
        if d in st:
            continue
        bns = 0
        L = 1
        for x in nums:
            if d % x == 0:
                L = lcm(L, x)
                bns += 1
        if L == d and bns > ans:
            ans = bns
    print(ans)
