# _*_ coding: utf-8 _*_
# @Time : 2022/10/19 9:46 PM 
# @Author : yefe
# @File : 1976_count_paths

from collections import defaultdict
from functools import cache
from typing import List

INF = 0x3f3f3f3f
MOD = 10 ** 9 + 7


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_tbl = defaultdict(list)

        for u, v, t in roads:
            adj_tbl[u].append((v, t))
            adj_tbl[v].append((u, t))

        dist = [INF] * n
        seen = [False] * n

        dist[0] = 0

        for i in range(n):
            u = None
            d = INF
            for j in range(n):
                if not seen[j] and (not u or d < dist[u]):
                    u = j
                    d = dist[j]
            print(u)

            seen[u] = True
            for v, t in adj_tbl[u]:
                if dist[u] + t < dist[v]:
                    dist[v] = dist[u] + t

        print(dist)

        g = [[] for _ in range(n)]

        for u, v, t in roads:
            if dist[v] - dist[u] == t:
                g[v].append(u)
            if dist[u] - dist[v] == t:
                g[u].append(v)
        print(g)

        @cache
        def dfs(i):
            if i == 0:
                return 1

            ret = 0
            for j in g[i]:
                ret += dfs(j)
            return ret % MOD

        ans = dfs(n-1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 7
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5],
             [4, 6, 2]]

    ans = sol.countPaths(n, roads)
    print(ans)
