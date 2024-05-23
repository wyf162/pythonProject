# -*- coding: utf-8 -*-
# @Time: 2024/5/23 15:23
# @Author: yfwang
# @File: 501D.py
# 康托展开

import sys

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


class FenwickTree:
    def __init__(self, n, iter=None):
        self.n = n
        if iter is not None:
            self.bit = list(iter)

            for i in range(self.n):
                if i | (i + 1) < self.n:
                    self.bit[i | (i + 1)] += self.bit[i]
        else:
            self.bit = [0] * n
        length = (self.n + 1).bit_length() - 1
        self.powers = [1 << i for i in range(length, -1, -1)]
        self.tot = 0

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
        self.tot += delta

    def bisect_min_larger(self, num):
        if num <= 0: return -1
        note = -1
        tmp = 0
        for power in self.powers:
            if note + power >= self.n or \
                tmp + self.bit[note + power] >= num: continue
            note += power
            tmp += self.bit[note]
        return note + 1

    def bisect_max_smaller(self, num):
        if num > self.tot: return self.n
        note = -1
        tmp = 0
        for power in self.powers:
            if note + power >= self.n or \
                tmp + self.bit[note + power] >= num: continue
            note += power
            tmp += self.bit[note]
        return note


n = I()
perm1 = LI()
order1 = [0] * n

fen = FenwickTree(n)
for i in range(n):
    order1[i] = perm1[i] - fen.sum(perm1[i])
    fen.add(perm1[i], 1)

perm2 = LI()
order2 = [0] * n

fen = FenwickTree(n)
for i in range(n):
    order2[i] = perm2[i] - fen.sum(perm2[i])
    fen.add(perm2[i], 1)

order = [0] * n
carry = 0
for i in range(n - 1, -1, -1):
    carry, order[i] = divmod(order1[i] + order2[i] + carry, n - i)

ans = [0] * n
fen = FenwickTree(n, [1] * n)
for i in range(n):
    ans[i] = fen.bisect_min_larger(order[i] + 1)
    fen.add(ans[i], -1)

print(' '.join(map(str, ans)))

