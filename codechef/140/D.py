# -*- coding : utf-8 -*-
# @Time: 2024/6/26 23:01
# @Author: yefei.wang
# @File: D.py

import sys
import random

n = 3 * 10 ** 5 + 5
times = random.randint(100, 500)
mod = random.getrandbits(32)
powers = [1] * (n + 1)
for i in range(1, n + 1):
    powers[i] = powers[i - 1] * times % mod


class RollingHash:
    def __init__(self, s):
        self.val = [0]
        for c in s:
            self.val.append((self.val[-1] * times + ord(c)) % mod)

    def substr(self, i, j):
        if j < i:
            return 0
        return (self.val[j + 1] - self.val[i] * powers[j - i + 1]) % mod


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')


tcn = I()
for _tcn_ in range(tcn):
    s = input()
    n = len(s)
    if n % 2:
        print(0)
        continue
    rh = RollingHash(s)
    k = n // 2
    ans = 0
    for i in range(n // 2 + 1):
        x1 = rh.substr(0, i - 1)
        x2 = rh.substr(i, i + k - 1)
        x3 = rh.substr(i + k, n - 1)

        x4 = (x1 * powers[n - i - k] + x3) % mod
        if x4 == x2:
            ans += 1
    print(ans)
