# -*- coding : utf-8 -*-
# @Time: 2022/8/11 21:02
# @Author: yefei.wang
# @File: 1697_distance_limited_paths_exist.py
from typing import List


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
    def distanceLimitedPathsExist(self,
                                  n: int,
                                  edgeList: List[List[int]],
                                  queries: List[List[int]]) -> List[bool]:

        uf = UnionFind(n)

        for idx, query in enumerate(queries):
            query.append(idx)

        queries.sort(key=lambda x: x[2])

        edgeList.sort(key=lambda x: x[2])

        ans = [False] * (len(queries))

        i = 0
        for query in queries:
            while i < len(edgeList) and edgeList[i][2] < query[2]:
                uf.merge(edgeList[i][0], edgeList[i][1])
                i += 1
            ans[query[3]] = uf.are_connected(query[0], query[1])

        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 3
    edgeList = [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]]
    queries = [[0, 1, 2], [0, 2, 5]]
    ret = sol.distanceLimitedPathsExist(n, edgeList, queries)
    print(ret)

