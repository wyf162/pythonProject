# -*- coding : utf-8 -*-
# @Time: 2024/7/28 10:57
# @Author: yefei.wang
# @File: D.py

import typing
from typing import List


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
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        n = len(circles)
        dsu = DSU(n)
        for i in range(n):
            for j in range(i, n, 1):
                x1, y1, r1 = circles[i]
                x2, y2, r2 = circles[j]
                dx, dy = x2 - x1, y2 - y1
                if dx * dx + dy * dy <= (r1 + r2) * (r1 + r2):
                    dsu.merge(i, j)

        ans = True
        for group in dsu.groups():
            top_left = False
            down_right = False
            for i in group:
                # y = Y
                x1, y1, r1 = circles[i]
                if abs(y1 - Y) <= r1 or abs(x1 - 0) <= r1:
                    top_left = True

                if abs(y1 - 0) <= r1 or abs(x1 - X) <= r1:
                    down_right = True

            if top_left and down_right:
                ans = False
        return ans


if __name__ == '__main__':
    sol = Solution()
    X = 3
    Y = 3
    circles = [[2, 4, 1], [4, 4, 1], [4, 2, 1]]
    ret = sol.canReachCorner(X, Y, circles)
    print(ret)
