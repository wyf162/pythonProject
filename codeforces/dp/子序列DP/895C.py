# -*- coding: utf-8 -*-
# @Time: 2024/3/7 9:21
# @Author: yfwang
# @File: 895C.py
# https://codeforces.com/problemset/problem/895/C

import sys
from collections import Counter

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

# constants
MOD = 10 ** 9 + 7
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]


def tomask(x):
    mask = 0
    for i, p in enumerate(primes):
        deg = 0
        while x % p == 0:
            x //= p
            deg += 1
        mask |= (deg & 1) << i

    return mask


# init
N = 1 << len(primes)
two = [1] * (N + 1)
for i in range(1, N + 1):
    two[i] = two[i - 1] * 2 % MOD

# read input
n = int(input())
a = map(int, input().split())

counter = [0] * N
for x in a:
    counter[tomask(x)] += 1

# dp calculation
dp = [0] * N
dp[0] = 1
for cmask, cnt in enumerate(counter):
    if cnt == 0:
        continue

    newdp = [0] * N
    for mask in range(0, N):
        newdp[mask ^ cmask] = (newdp[mask ^ cmask] + dp[mask] * two[cnt - 1]) % MOD
        newdp[mask] = (newdp[mask] + dp[mask] * two[cnt - 1]) % MOD

    dp, newdp = newdp, dp

print((dp[0] - 1) % MOD)
