# -*- coding: utf-8 -*-
# @Time: 2024/7/8 13:28
# @Author: yfwang
# @File: 3203.py

from collections import deque
from typing import List


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        def get_diameter(edges):
            n = len(edges) + 1
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)

            def bfs(start):
                q = deque([(start, -1)])
                step = -1
                while q:
                    step += 1
                    for _ in range(len(q)):
                        x, fa = q.popleft()
                        for y in g[x]:
                            if y != fa:
                                q.append((y, x))
                return step, x

            mx1, v1 = bfs(0)
            mx2, v2 = bfs(v1)
            return mx2

        d1 = get_diameter(edges1)
        d2 = get_diameter(edges2)
        ans = max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)
        return ans
