# -*- coding : utf-8 -*-
# @Time: 2024/3/6 23:14
# @Author: yefei.wang
# @File: G.py


import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, x = MI()
    prime_factors = []
    p = 2
    while p * p <= x:
        pw = 0
        while x % p == 0:
            x //= p
            pw += 1
        if pw > 0:
            prime_factors.append((p, pw))
        p += 1
    if x > 1:
        prime_factors.append((x, 1))
    ans = 0
    for l in range(1, n + 1):
        ways = 1
        for p, pw in prime_factors:
            ways = ways * (pow(pw + 1, l, mod) - pow(pw, l, mod)) % mod
        ans += ways
    print(ans % mod)
