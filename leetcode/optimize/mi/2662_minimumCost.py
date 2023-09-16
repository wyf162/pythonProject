# -*- coding : utf-8 -*-
# @Time: 2023/9/16 14:32
# @Author: yefei.wang
# @File: 2662_minimumCost.py
import heapq
from collections import defaultdict
from math import inf
from typing import List


def coord2num(x1, y1):
    return x1 * 100001 + y1


def num2coord(num):
    return num // 100001, num % 100001


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        # vertex set
        vs = set()
        vf = coord2num(*start)
        ve = coord2num(*target)
        vs.add(vf)
        vs.add(ve)
        adj_tbl = defaultdict(dict)
        for special_road in specialRoads:
            x1, y1, x2, y2, c = special_road
            v1, v2 = coord2num(x1, y1), coord2num(x2, y2)
            vs.add(v1)
            vs.add(v2)
            adj_tbl[v1][v2] = min(c, dist(x1, y1, x2, y2), adj_tbl.get(v1, dict()).get(v2, inf))

        vl = list(sorted(vs))
        for i in range(len(vl)):
            for j in range(len(vl)):
                if i == j: continue
                v1, v2 = vl[i], vl[j]
                x1, y1 = num2coord(v1)
                x2, y2 = num2coord(v2)
                adj_tbl[v1][v2] = min(adj_tbl.get(v1, dict()).get(v2, inf), dist(x1, y1, x2, y2))

        dis = defaultdict(lambda:float("inf"))
        dis[vf] = 0
        q = [(0, vf)]
        vis = set()
        while q:
            _, u = heapq.heappop(q)
            if u in vis: continue
            vis.add(u)
            for v, w in adj_tbl[u].items():
                if dis[v] > dis[u] + w:
                    dis[v] = dis[u] + w
                    heapq.heappush(q, (dis[v], v))
        return dis[ve]


if __name__ == '__main__':
    sol = Solution()
    start = [1, 1]
    target = [100000,100000]
    specialRoads = [[1,1,100000,99999,19999]]
    ret = sol.minimumCost(start, target, specialRoads)
    print(ret)
