# -*- coding : utf-8 -*-
# @Time: 2023/10/2 0:19
# @Author: yefei.wang
# @File: 1786_countRestrictedPaths.py

from collections import deque
from heapq import heappush, heappop
from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        deg = [0] * n
        for u, v, w in edges:
            u -= 1
            v -= 1
            g[u].append([v, w])
            g[v].append([u, w])
            deg[u] += 1
            deg[v] += 1

        pq = []
        heappush(pq, [0, n - 1])
        dist = dict()
        dist[n - 1] = 0
        while pq:
            d, x = heappop(pq)
            for y, w in g[x]:
                if y not in dist or dist[y] > d + w:
                    dist[y] = d + w
                    heappush(pq, [d + w, y])

        dp = [0] * n
        dp[0] = 1
        pq = []
        heappush(pq, [-dist[0], 0])
        vis = set()

        while pq:
            d, x = heappop(pq)
            if x in vis:
                continue
            vis.add(x)
            for y, _ in g[x]:
                if dist[y] < dist[x]:
                    dp[y] += dp[x]
                    heappush(pq, [-dist[y], y])
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    n = 9
    edges = [[6, 2, 35129], [3, 4, 99499], [2, 7, 43547], [8, 1, 78671], [2, 1, 66308], [9, 6, 33462], [5, 1, 48249],
             [2, 3, 44414], [6, 7, 44602], [1, 7, 14931], [8, 9, 38171], [4, 5, 30827], [3, 9, 79166], [4, 8, 93731],
             [5, 9, 64068], [7, 5, 17741], [6, 3, 76017], [9, 4, 72244]]
    # edges = [[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1], [5, 4, 10]]
    ret = sol.countRestrictedPaths(n, edges)
    print(ret)
