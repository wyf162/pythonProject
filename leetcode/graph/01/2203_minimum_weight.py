# _*_ coding: utf-8 _*_
# @Time : 2022/11/26 3:19 PM 
# @Author : yefe
# @File : 2203_minimum_weight

from typing import List
from collections import defaultdict
from heapq import heappop, heappush

INT_MAX = 0xff3f3f3f


class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]

        for u, v, w in edges:
            g[u].append([v, w])
            rg[v].append([u, w])

        dis1 = self.dijkstra(g, src1)
        dis2 = self.dijkstra(g, src2)
        dis3 = self.dijkstra(rg, dest)

        ret = INT_MAX
        for i in range(n):
            ret = min(ret, dis1[i]+dis2[i]+dis3[i])
        return ret if ret<INT_MAX else -1


    @staticmethod
    def dijkstra(g: List[List[int]], src: int) -> List[int]:
        n = len(g)
        dis = [INT_MAX for _ in range(n)]
        dis[src] = 0
        pq = [(0, src)]
        vis = set()

        while pq:
            _, u = heappop(pq)
            if u in vis:
                continue
            vis.add(u)
            for v, w in g[u]:
                if dis[v]>dis[u]+w:
                    dis[v] = dis[u]+w
                    heappush(pq, (dis[v], v))
        return dis


if __name__ == '__main__':
    sol = Solution()
    n = 6
    edges = [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3], [2, 3, 4], [3, 4, 2],
                    [4, 5, 1]]
    src1 = 0
    src2 = 1
    dest = 5
    ret = sol.minimumWeight(n, edges, src1, src2, dest)
    print(ret)
