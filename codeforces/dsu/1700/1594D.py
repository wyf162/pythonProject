# -*- coding: utf-8 -*-
# @Time: 2024/7/17 11:21
# @Author: yfwang
# @File: 1594D.py

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

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    dsu = DSU(n + n)
    for _ in range(m):
        u, v, s = input().split()
        u = int(u) - 1
        v = int(v) - 1
        if s == 'imposter':
            dsu.merge(u, v + n)
            dsu.merge(v, u + n)
        else:
            dsu.merge(u, v)
            dsu.merge(v + n, u + n)

    paradox = False
    for x in range(n):
        if dsu.same(x, x + n):
            paradox = True
    if paradox:
        print(-1)
        continue

    groups = [[] for _ in range(n + n)]
    for x in range(n + n):
        fx = dsu.leader(x)
        groups[fx].append(x)

    ans = 0
    vis = set()
    for x in range(n):
        fx = dsu.leader(x)
        fy = dsu.leader(x + n)
        if fx in vis or fy in vis:
            continue
        vis.add(fx)
        vis.add(fy)
        c1 = 0
        for v in groups[fx]:
            c1 += int(v < n)
        c2 = 0
        for v in groups[fy]:
            c2 += int(v < n)
        ans += max(c1, c2)

    print(ans)



