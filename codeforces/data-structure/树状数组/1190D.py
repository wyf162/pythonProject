# -*- coding: utf-8 -*-
# @Time: 2024/5/29 13:44
# @Author: yfwang
# @File: 1190D.py
# https://codeforces.com/problemset/problem/1190/D

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

tcn = 4
for _tcn_ in range(tcn):
    n = I()
    points = [LI() for _ in range(n)]
    xs = [points[i][0] for i in range(n)]
    ys = [points[i][1] for i in range(n)]
    x2i = {v: i for i, v in enumerate(sorted(set(xs)))}
    y2j = {v: i for i, v in enumerate(sorted(set(ys)))}

    points = [[x2i[x], y2j[y]] for x, y in points]

    fwt = FenwickTree(len(x2i))
    check = [0] * len(x2i)

    groups = [[] for _ in range(n)]
    for x, y in points:
        groups[y].append(x)

    for group in groups:
        group.sort()

    ans = 0
    for y in sorted(y2j.values(), reverse=True):
        for x in groups[y]:
            if check[x] == 0:
                fwt.add(x, 1)
                check[x] = 1
        for x1, x2 in zip([-1] + groups[y][:-1], groups[y][:]):
            ans += (fwt.sum(x1 + 1, x2) + 1) * (fwt.sum(x2 + 1, len(x2i)) + 1)
    print(ans)
