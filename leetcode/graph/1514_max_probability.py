# _*_ coding: utf-8 _*_
# @Time : 2022/05/03 5:11 PM 
# @Author : yefe
# @File : 1514_max_probability
from typing import List
import heapq
from collections import defaultdict


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (x, y) in enumerate(edges):
            graph[x].append((succProb[i], y))
            graph[y].append((succProb[i], x))

        que = [(-1.0, start)]
        prob = [0.0] * n
        prob[start] = 1.0

        while que:
            pr, node = heapq.heappop(que)
            pr = -pr
            if pr < prob[node]:
                continue
            for prNext, nodeNext in graph[node]:
                if prob[nodeNext] < prob[node] * prNext:
                    prob[nodeNext] = prob[node] * prNext
                    heapq.heappush(que, (-prob[nodeNext], nodeNext))
        return prob[end]
