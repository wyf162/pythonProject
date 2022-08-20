# _*_ coding: utf-8 _*_
# @Time : 2022/08/15 11:15 PM 
# @Author : yefe
# @File : 1192_criticalConnections
from typing import List
from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        adj_tbl = defaultdict(set)
        for u, v in connections:
            adj_tbl[u].add(v)
            adj_tbl[v].add(u)

        dfn = [0 for _ in range(n)]
        low = [0 for _ in range(n)]

        ts = 1
        res = []

        def tarjan(x: int, parent: int) -> None:
            nonlocal ts
            dfn[x] = ts
            low[x] = ts
            ts += 1
            for y in adj_tbl[x]:
                if y == parent:
                    continue

                if dfn[y] == 0:
                    tarjan(y, x)
                    low[x] = min(low[x], low[y])

                    if low[y] >= dfn[x]:
                        res.append(x)
                elif dfn[y] != 0:
                    low[x] = min(low[x], dfn[y])

        tarjan(0, -1)
        return res


if __name__ == '__main__':
    sol = Solution()
    n = 4
    connections = [[1, 2], [1, 3], [2, 3], [1, 0]]
    ret = sol.criticalConnections(n, connections)
    print(ret)
