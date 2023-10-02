# -*- coding : utf-8 -*-
# @Time: 2023/10/1 21:58
# @Author: yefei.wang
# @File: 1514.py

from typing import List
from math import log, exp
from heapq import heappop, heappush


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:

        g = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            w = log(1/succProb[i])
            g[u].append([v, w])
            g[v].append([u, w])

        pq = []
        heappush(pq, [0, start_node])
        dist = dict()
        while pq:
            d, x = heappop(pq)
            for y, w in g[x]:
                if y not in dist or dist[y] > d + w:
                    dist[y] = d+w
                    heappush(pq, [d+w, y])

        if end_node not in dist:
            return 0
        else:
            return 1 / exp(dist[end_node])
