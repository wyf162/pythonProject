# -*- coding: utf-8 -*-
# @Time: 2024/4/22 16:19
# @Author: yfwang
# @File: 3123.py

from typing import List
from heapq import heappush, heappop
from collections import Counter


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        pq = []
        heappush(pq, [0, 0])
        dist = Counter()
        dist[0] = 0
        while pq:
            d, x = heappop(pq)
            for y, w in g[x]:
                if y not in dist or dist[y] > d + w:
                    dist[y] = d + w
                    heappush(pq, [d + w, y])

        st = set()
        pq = [(dist[n - 1], n - 1)]
        while pq:
            d, x = heappop(pq)
            for y, w in g[x]:
                if dist[y] == d - w:
                    st.add((x, y))
                    heappush(pq, (d - w, y))
        m = len(edges)
        ans = [False] * m
        for i in range(m):
            u, v, w = edges[i]
            if (u, v) in st or (v, u) in st:
                ans[i] = True
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 6
    edges = [[0, 1, 4], [0, 2, 1], [1, 3, 2], [1, 4, 3], [1, 5, 1], [2, 3, 1], [3, 5, 3], [4, 5, 2]]
    ret = sol.findAnswer(n,edges)
    print(ret)
