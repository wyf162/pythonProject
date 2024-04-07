# -*- coding : utf-8 -*-
# @Time: 2024/4/7 10:29
# @Author: yefei.wang
# @File: D.py

from typing import List

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


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu = DSU(n)
        ws = [[] for _ in range(n)]
        for u, v, w in edges:
            dsu.merge(u, v)
            ws[u].append(w)
            ws[v].append(w)

        hst = dict()
        for group in dsu.groups():
            v = (1 << 32) - 1
            for x in group:
                for w in ws[x]:
                    v &= w
            if v < (1 << 31):
                hst[dsu.leader(group[0])] = v
            else:
                hst[dsu.leader(group[0])] = 0
        ans = []
        for x, y in query:
            fx = dsu.leader(x)
            fy = dsu.leader(y)
            if x == y:
                ans.append(0)
            elif fx == fy:
                ans.append(hst[fx])
            else:
                ans.append(-1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 9
    edges = [[0, 4, 7], [3, 5, 1], [1, 3, 5], [1, 5, 1]]
    query = [[0, 4], [1, 5], [3, 0], [3, 3], [3, 2], [2, 0], [7, 7], [7, 0]]
    ret = sol.minimumCost(n, edges, query)
    print(ret)
