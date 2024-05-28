# -*- coding : utf-8 -*-
# @Time: 2024/5/27 22:31
# @Author: yefei.wang
# @File: 1185C2.py

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
        if num <= 0:
            return -1
        note = -1
        tmp = 0
        for power in self.powers:
            if note + power >= self.n or tmp + self.bit[note + power] > num:
                continue
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

tcn = 2
for _tcn_ in range(tcn):
    n, m = MI()
    nums = LI()
    ans = [0] * n
    v2i = list(sorted(range(n), key=lambda i: nums[i]))
    ind = [0] * n
    for i, x in enumerate(v2i):
        ind[x] = i
    fwt1 = FenwickTree(n)
    fwt2 = FenwickTree(n)

    for i in range(n):
        j1 = fwt1.bisect_min_larger(m - nums[i])
        # print('min_larger', j1, fwt1.sum(min(j1, n - 1)), m - nums[i])

        # j0 = fwt1.bisect_max_smaller(m - nums[i])
        # print('max_smaller', j0, fwt1.sum(min(j0, n - 1)), m - nums[i])
        j2 = fwt2.sum(j1 - 1)
        ans[i] = i - j2
        fwt1.add(ind[i], nums[i])
        fwt2.add(ind[i], 1)

    print(*ans)
