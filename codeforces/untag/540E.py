# -*- coding: utf-8 -*-
# @Time: 2024/4/12 10:56
# @Author: yfwang
# @File: 540E.py
# https://codeforces.com/problemset/problem/540/E

import typing


class FenwickTree:
    """
    Reference: https://en.wikipedia.org/wiki/Fenwick_tree
    https://github.com/atcoder/ac-library/blob/master/document_en/fenwicktree.md
    """

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
swaps = [LI() for _ in range(n)]
hst = dict()
for a, b in swaps:
    if a not in hst:
        hst[a] = a
    if b not in hst:
        hst[b] = b

    hst[a], hst[b] = hst[b], hst[a]

pos = {v: i for i, v in hst.items()}
pts = sorted(hst)
map_pos = {v: i * 2 for i, v in enumerate(pts)}

n = len(hst)
fen = FenwickTree(2 * n - 1)

ans = 0
for i in range(n - 1, -1, -1):
    if i < n - 1:
        p = 2 * i + 1
        ans += fen.sum(0, p) * (pts[i + 1] - pts[i] - 1)
        fen.add(p, pts[i + 1] - pts[i] - 1)
    p = map_pos[pos[pts[i]]]
    ans += fen.sum(0, p)
    fen.add(p, 1)
print(ans)
