# -*- coding : utf-8 -*-
# @Time: 2024/3/15 23:28
# @Author: yefei.wang
# @File: D.py


import sys
import random

n = 5005
times = random.randint(100, 500)
mod = random.getrandbits(32)
powers = [1] * (n + 1)
for i in range(1, n + 1):
    powers[i] = powers[i - 1] * times % mod


class RollingHash:
    def __init__(self, s):
        self.pre = [0]
        for c in s:
            self.pre.append((self.pre[-1] * times + ord(c)) % mod)

        self.suf = [0]
        for i, c in enumerate(s[::-1]):
            self.suf.append((self.suf[-1] + ord(c) * powers[i]) % mod)

    def pre_substr(self, i):
        return self.pre[i]

    def suf_substr(self, i):
        return self.suf[i]


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(n):
    s



