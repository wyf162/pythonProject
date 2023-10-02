# _*_ coding: utf-8 _*_
# @Time : 2022/08/27 9:21 PM 
# @Author : yefe
# @File : 847_shortest_path_length

from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        M = 0x3f3f3f3f
        n = len(graph)
        d = [[n + 1] * n for _ in range(n)]

        for i in range(n):
            for j in graph[i]:
                d[i][j] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        f = [[M] * (1 << n) for _ in range(n)]

        for mask in range(1, 1 << n):
            if (mask & (mask - 1)) == 0:
                u = bin(mask).count("0") - 1
                f[u][mask] = 0
            else:
                for u in range(n):
                    if mask & (1 << u):
                        for v in range(n):
                            if (mask & (1 << v)) and u != v:
                                f[u][mask] = min(f[u][mask], f[v][mask ^ (1 << u)] + d[v][u])

        ans = min(f[u][(1 << n) - 1] for u in range(n))
        return ans


if __name__ == '__main__':
    sol = Solution()
    graph = [[1, 2, 3], [0], [0], [0]]
    ret = sol.shortestPathLength(graph)
    print(ret)
