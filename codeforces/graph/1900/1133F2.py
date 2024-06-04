# -*- coding: utf-8 -*-
# @Time: 2024/6/4 11:19
# @Author: yfwang
# @File: 1133F2.py
# mst

import sys
import typing


class DSU:
    '''
    Implement (union by size) + (path halving)

    Reference:
    Zvi Galil and Giuseppe F. Italiano,
    Data structures and algorithms for disjoint set union problems
    '''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n

        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]]
            )

        return a

    def size(self, a: int) -> int:
        assert 0 <= a < self._n

        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> typing.List[typing.List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]

        result: typing.List[typing.List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))


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

tcn = 3
for _tcn_ in range(tcn):
    n, m, D = MI()
    edges = [LGMI() for _ in range(m)]

    dsu1 = DSU(n)
    dsu2 = DSU(n)
    deg = 0
    for x, y in edges:
        dsu1.merge(x, y)
        if x == 0 or y == 0:
            deg += 1
        else:
            dsu2.merge(x, y)

    groups1 = dsu1.groups()
    groups2 = dsu2.groups()

    if deg < D:
        YN(False)
    else:
        if len(groups1) == 1 and len(groups2) - 1 <= D:
            YN(True)
            vis = [0] * len(groups2)
            v2g = [0] * n
            for i, group in enumerate(groups2):
                for x in group:
                    v2g[x] = i
            ans = []

            ee = []
            g = [[] for _ in range(n)]
            for x, y in edges:
                g[x].append(y)
                g[y].append(x)
                if x == 0 or y == 0:
                    ee.append((x, y))

            dsu3 = DSU(n)
            d = D
            for x, y in ee:
                if y == 0:
                    x, y = y, x

                if not vis[v2g[y]]:
                    ans.append((x, y))
                    vis[v2g[y]] = 1
                    dsu3.merge(x, y)
                    d -= 1
            for x, y in ee:
                if d == 0:
                    break
                if dsu3.same(x, y):
                    continue
                else:
                    ans.append((x, y))
                    dsu3.merge(x, y)
                    d -= 1

            for x, y in edges:
                if dsu3.same(x, y) or x == 0 or y == 0:
                    continue
                else:
                    ans.append((x, y))
                    dsu3.merge(x, y)
            for x, y in ans:
                print(x+1, y + 1)

        else:
            YN(False)
