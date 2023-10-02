# -*- coding : utf-8 -*-
# @Time: 2023/10/1 21:45
# @Author: yefei.wang
# @File: 1334.py
from collections import deque, Counter
from typing import List
from heapq import heappop, heappush


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append([v, w])
            g[v].append([u, w])

        mi = 100
        ans = -1
        for i in range(n):
            pq = []
            heappush(pq, [0, i])
            dist = Counter()
            dist[i] = 0
            while pq:
                d, x = heappop(pq)
                for y, w in g[x]:
                    if (y not in dist or dist[y] > d + w) and d + w <= distanceThreshold:
                        heappush(pq, [d + w, y])
                        dist[y] = d + w

            if len(dist) <= mi:
                ans = i
                mi = len(dist)
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 6
    edges = [[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]]
    distanceThreshold = 20
    ret = sol.findTheCity(n, edges, distanceThreshold)
    print(ret)
