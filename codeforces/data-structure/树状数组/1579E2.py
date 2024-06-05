# -*- coding: utf-8 -*-
# @Time: 2024/6/5 10:40
# @Author: yfwang
# @File: 1579E2.py


import sys


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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    v2i = {v: i for i, v in enumerate(sorted(set(A)))}
    fwt = FenwickTree(n)

    ans = 0
    for i, a in enumerate(A):
        j = v2i[a]
        c1 = fwt.sum(0, j)
        c2 = fwt.sum(j + 1, n)
        ans += min(c1, c2)
        fwt.add(j, 1)
    print(ans)
