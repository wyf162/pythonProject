# -*- coding: utf-8 -*-
# @Time: 2024/5/22 10:33
# @Author: yfwang
# @File: 314C.py
# https://codeforces.com/problemset/problem/314/C
# LIS

class FenwickTree:
    """
    Reference: https://en.wikipedia.org/wiki/Fenwick_tree
    https://github.com/atcoder/ac-library/blob/master/document_en/fenwicktree.md
    """

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: int) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> int:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> int:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


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

tcn = 5
for _tcn_ in range(tcn):
    N = 10 ** 6 + 5
    op = lambda a, b: a + b
    e = 0
    Lst = FenwickTree(N)
    Lst.add(0, 1)
    n = I()
    nums = LI()
    f = [0] * N
    for x in nums:
        add = (Lst.sum(0, x + 1) * x - f[x]) % mod
        f[x] += add
        f[x] %= mod
        Lst.add(x, add)
    ans = sum(f) % mod
    print(ans)
