# _*_ coding: utf-8 _*_
# @Time : 2021/11/7 下午3:48 
# @Author : wangyefei
# @File : 5921_maximalPathQuality.py

from copy import deepcopy
from typing import List
import heapq

MAX_PATH = 999999999


class Node(object):
    def __init__(self, cur, time, val):
        self.cur = cur
        self.time = time
        self.val = val

    def compute(self, vals):
        ans = 0
        print(self.val)
        for v in self.val:
            ans += vals[v]
        return ans


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        hst = {}
        hst_time = {}
        for edge in edges:
            hst[edge[0]] = hst.get(edge[0], [])
            hst[edge[0]].append(edge[1])
            hst[edge[1]] = hst.get(edge[1], [])
            hst[edge[1]].append(edge[0])
            hst_time[(edge[0], edge[1])] = edge[2]
            hst_time[(edge[1], edge[0])] = edge[2]
        print(hst)
        print(hst_time)
        min_path = self.dijkstra(len(values), edges)

        start_node = Node(0, maxTime, {0})
        q = [start_node]
        ans = values[0]
        while q:
            node = q.pop(0)
            cur = node.cur
            for nex in hst.get(cur, []):
                new_time = node.time - hst_time[(cur, nex)]
                if new_time >= 0 and node.time - min_path[nex]>=0:
                    new_set = deepcopy(node.val)
                    new_set.add(nex)
                    new_node = Node(nex, new_time, new_set)
                    if nex == 0:
                        ans = max(ans, new_node.compute(values))
                    q.append(new_node)
        return ans

    def dijkstra(self, n, edges):
        hst = {}
        for edge in edges:
            hst[(edge[0], edge[1])] = edge[2]
            hst[(edge[1], edge[0])] = edge[2]
        adj_tbl = {}
        for u, v, w in edges:
            adj_tbl[u] = adj_tbl.get(u, [])
            adj_tbl[u].append(v)
            adj_tbl[v] = adj_tbl.get(v, [])
            adj_tbl[v].append(u)

        dis = [0] + [MAX_PATH] * n
        vis = [True] + [False] * n
        for i in range(1, n + 1):
            if hst.get((0, i)):
                dis[i] = hst.get((0, i))
        while not all(vis):
            print(vis)
            u, d = 0, MAX_PATH
            for i in range(1, n + 1):
                if not vis[i] and dis[i] <= d:
                    u, d = i, dis[i]
            vis[u] = True

            for i in range(1, n + 1):
                if hst.get((i, u)) and dis[i] + hst[(i, u)] < dis[u]:
                    dis[u] = dis[i] + hst[(i, u)]

        return dis


if __name__ == "__main__":
    # n = 4
    # edges = [[0, 1, 3], [0, 2, 2], [1, 2, 5], [2, 3, 7], [1, 3, 4], [1, 4, 6]]
    values = [5, 10, 15, 20]
    edges = [[0, 1, 10], [1, 2, 10], [0, 3, 10]]
    maxTime = 30
    sol = Solution()
    dis = sol.maximalPathQuality(values, edges, maxTime)
    print(dis)
