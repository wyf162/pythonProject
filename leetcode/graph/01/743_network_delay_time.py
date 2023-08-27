# _*_ coding: utf-8 _*_
# @Time : 2022/11/26 8:41 PM 
# @Author : yefe
# @File : 743_network_delay_time

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


INT_MAX = 0x3f3f3f3f


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)

        for u, v, w in times:
            g[u].append([v, w])

        dis = [INT_MAX]*(n+1)
        dis[k] = 0
        pq = [(0, k)]
        vis = set()

        while pq:
            _, u = heappop(pq)
            if u in vis:
                continue
            vis.add(u)

            for v, w in g[u]:
                if dis[v]>dis[u]+w:
                    dis[v]=dis[u]+w
                    heappush(pq, (dis[v], v))

        return max(dis[1:])


if __name__ == '__main__':
    sol = Solution()
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    ret = sol.networkDelayTime(times, n, k)
    print(ret)
