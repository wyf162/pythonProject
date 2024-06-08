# -*- coding : utf-8 -*-
# @Time: 2024/6/7 19:21
# @Author: yefei.wang
# @File: C.py

import sys
import typing
import bisect


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
sys.stdin = open('../../../input.txt', 'r')
sys.stdout = open('../../../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('Yes' if x else 'No')
mod = 1000000007
mod2 = 998244353

n = I()
A = LI()
m = I()
queries = [LI() for i in range(m)]

xi = [(i, a) for i, a in enumerate(A)]
xi.sort(key=lambda x: -x[1])
vis = [0] * n
dsu = DSU(n)

B = []
C = []

for i, a in xi:
    vis[i] = 1
    if i - 1 >= 0 and vis[i - 1]:
        dsu.merge(i - 1, i)
    if i + 1 < n and vis[i + 1]:
        dsu.merge(i + 1, i)
    B.append(a)
    if C:
        C.append(max(C[-1], dsu.size(i)))
    else:
        C.append(dsu.size(i))


B.reverse()
C.reverse()

for val, mi, mx in queries:
    i = bisect.bisect_left(B, val)
    if i < n and C[i] >= mi:
        YN(True)
    else:
        YN(False)

