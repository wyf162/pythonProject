# -*- coding : utf-8 -*-
# @Time: 2023/10/1 18:55
# @Author: yefei.wang
# @File: 1928_minCost.py

from typing import List, Tuple
from heapq import heappop, heappush


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        adjList = [[] for _ in range(n)]
        for u, v, t in edges:
            adjList[u].append([v, t])
            adjList[v].append([u, t])

        times = dict()
        pq = [[passingFees[0], 0, 0]]

        while pq:
            cur_cost, cur_id, cur_time = heappop(pq)
            if cur_time > maxTime:
                continue
            if cur_id == n-1:
                return cur_cost

            if cur_id not in times or times[cur_id] < cur_time:
                times[cur_id] = cur_time
                for next_id, next_time in adjList[cur_id]:
                    heappush(pq, [cur_cost + passingFees[next_id], next_id, cur_time + next_time])
        return -1
