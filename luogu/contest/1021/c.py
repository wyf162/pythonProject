# -*- coding : utf-8 -*-
# @Time: 2023/10/21 12:44
# @Author: yefei.wang
# @File: c.py

import math
import sys

sys.stdin = open('./../../input.txt', 'r')
sys.stdout = open('./../../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn, m = MI()
for _tcn_ in range(tcn):
    a, b, c = MI()
    delta = b * b - 4 * a * c
    if delta < 0:
        print('NO')
        continue
    i = 2
    sqrt_delta = delta
    while sqrt_delta >= i * i:
        while sqrt_delta % (i * i) == 0:
            sqrt_delta //= (i * i)
        i += 1
    if sqrt_delta == 0:
        b = -b
        b2a_signal = b * a
        b2a_gcd = math.gcd(b, 2 * a)
        p1 = abs(b) // b2a_gcd
        q1 = abs(2 * a) // b2a_gcd
        if b2a_signal != 0:
            if b2a_signal < 0:
                print('-', end='')
            print(p1, end='')
            if q1 > 1:
                print(f'/{q1}', end='')
        print('')
        continue

    if sqrt_delta == 1:
        b = -b + math.isqrt(delta // sqrt_delta)
        b2a_signal = b * a
        b2a_gcd = math.gcd(b, 2 * a)
        p1 = abs(b) // b2a_gcd
        q1 = abs(2 * a) // b2a_gcd
        if b2a_signal != 0:
            if b2a_signal < 0:
                print('-', end='')
            print(p1, end='')
            if q1 > 1:
                print(f'/{q1}', end='')
        print('')
        continue

    b2a_signal = -b * a
    b2a_gcd = math.gcd(b, 2 * a)
    p1 = abs(b) // b2a_gcd
    q1 = abs(2 * a) // b2a_gcd

    sqrt_p = math.isqrt(delta // sqrt_delta)
    d2a_gcd = math.gcd(sqrt_p, 2 * a)
    p2 = sqrt_p // d2a_gcd
    q2 = abs(2 * a) // d2a_gcd

    if b2a_signal != 0:
        if b2a_signal < 0:
            print('-', end='')
        print(p1, end='')
        if q1 > 1:
            print(f'/{q1}', end='')
        print('+', end='')
    if p2 > 1:
        print(p2, end='')
        print('*', end='')
    print(f'sqrt({sqrt_delta})', end='')
    if q2 > 1:
        print(f'/{q2}', end='')
    print('')
