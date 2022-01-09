# -*- coding : utf-8 -*-
# @Time: 2022/1/3 15:08
# @Author: yefei.wang
# @File: 310_find_min_height_trees.py
from typing import List
from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_tbl = [[] for _ in range(n)]
        deg = [0] * n
        for v, w in edges:
            adj_tbl[v].append(w)
            adj_tbl[w].append(v)
            deg[v] += 1
            deg[w] += 1

        q = deque(i for i, d in enumerate(deg) if d <= 1)
        cnt = n
        while cnt > 2:
            for i in range(len(q)):
                cnt -= 1
                v = q.popleft()
                for w in adj_tbl[v]:
                    deg[w] -= 1
                    if deg[w] == 1:
                        q.append(w)
        return list(q)


if __name__ == '__main__':
    sol = Solution()
    # n = 4
    # edges = [[1, 0], [1, 2], [1, 3]]
    # n = 6
    # edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    # n = 2
    # edges = [[0, 1]]
    n = 3
    edges = [[0, 1], [0, 2]]
    data = sol.findMinHeightTrees(n, edges)
    print(data)
