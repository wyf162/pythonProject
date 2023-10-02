# -*- coding : utf-8 -*-
# @Time: 2022/8/11 19:54
# @Author: yefei.wang
# @File: 1627_are_connected.py
from typing import List
from math import gcd


class UnionFind:

    def __init__(self, n):
        self.parent = [_ for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.parent[root_x] = root_y

    def are_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:

        uf = UnionFind(n + 1)

        for i in range(threshold + 1, n + 1):
            c = 2
            while i * c < n + 1:
                uf.merge(i, i * c)
                c += 1

        return [uf.are_connected(x, y) for x, y in queries]


if __name__ == '__main__':
    sol = Solution()
    n = 6
    threshold = 2
    queries = [[1, 4], [2, 5], [3, 6]]
    ret = sol.areConnected(n, threshold, queries)
    print(ret)
