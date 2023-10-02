# -*- coding : utf-8 -*-
# @Time: 2023/10/1 13:17
# @Author: yefei.wang
# @File: 10075.py

from typing import List
from collections import deque


class Solution:
    def countVisitedNodes(self, g: List[int]) -> List[int]:
        n = len(g)
        rg = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in enumerate(g):
            rg[y].append(x)
            deg[y] += 1

        q = deque(i for i, d in enumerate(deg) if d == 0)
        while q:
            x = q.popleft()
            y = g[x]
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)

        ans = [0] * n

        def rdfs(x: int, depth: int) -> None:
            ans[x] = depth
            for y in rg[x]:
                if deg[y] == 0:
                    rdfs(y, depth + 1)

        for i, d in enumerate(deg):
            if d <= 0:
                continue
            ring = []
            x = i
            while True:
                deg[x] = -1
                ring.append(x)
                x = g[x]
                if x == i:
                    break
            for x in ring:
                rdfs(x, len(ring))
        return ans
