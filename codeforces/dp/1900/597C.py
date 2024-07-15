# -*- coding: utf-8 -*-
# @Time: 2024/7/15 9:52
# @Author: yfwang
# @File: 597C.py
# LIS

import sys


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * n

    def sum(self, r):
        res = 0
        while r >= 0:
            res += self.bit[r]
            r = (r & (r + 1)) - 1
        return res

    def rsum(self, l, r):
        return self.sum(r) - self.sum(l - 1)

    def add(self, idx, delta):
        while idx < self.n:
            self.bit[idx] += delta
            idx = idx | (idx + 1)

    def init(self):
        for i in range(self.n):
            self.bit[i] = 0


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

tcn = 1
for _tcn_ in range(tcn):
    n, k = MI()
    nums = [I() for _ in range(n)]

    dp = [1] * n
    fen = FenwickTree(n)

    for _ in range(k):
        fen.init()
        for i in range(n):
            fen.add(nums[i], dp[i])
            dp[i] = fen.sum(nums[i] - 1)

    print(sum(dp))
