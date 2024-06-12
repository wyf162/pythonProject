# -*- coding: utf-8 -*-
# @Time: 2024/6/12 9:41
# @Author: yfwang
# @File: H1.py

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
sys.stdin = open('../../../input.txt', 'r')
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
    grid = [list(input()) for _ in range(n)]
    f = lambda i, j: i * m + j

    dsu = DSU(n * m)
    row = [0] * n
    col = [0] * m
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                continue
            row[i] += 1
            col[j] += 1
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '#':
                    dsu.merge(f(i, j), f(ni, nj))
    ans = max(n, m)

    for i in range(n):
        vis = set()
        for j in range(m):
            if grid[i][j] == '#':
                leader = dsu.leader(f(i, j))
                vis.add(leader)
            if i - 1 >= 0 and grid[i - 1][j] == '#':
                leader = dsu.leader(f(i - 1, j))
                vis.add(leader)
            if i + 1 < n and grid[i + 1][j] == '#':
                leader = dsu.leader(f(i + 1, j))
                vis.add(leader)
        tot = 0
        for x in vis:
            tot += dsu.size(x)
        tot += m
        tot -= row[i]
        ans = max(ans, tot)

    for j in range(m):
        vis = set()
        for i in range(n):
            if grid[i][j] == '#':
                leader = dsu.leader(f(i, j))
                vis.add(leader)
            if j - 1 >= 0 and grid[i][j - 1] == '#':
                leader = dsu.leader(f(i, j - 1))
                vis.add(leader)
            if j + 1 < m and grid[i][j + 1] == '#':
                leader = dsu.leader(f(i, j + 1))
                vis.add(leader)
        tot = 0
        for x in vis:
            tot += dsu.size(x)
        tot += n
        tot -= col[j]
        ans = max(ans, tot)

    print(ans)
