# -*- coding : utf-8 -*-
# @Time: 2022/1/3 17:41
# @Author: yefei.wang
# @File: offer2_106_is_bipartite.py
from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n

        def dfs(v, c):
            colors[v] = c
            for w in graph[v]:
                if colors[w] == 0:
                    colors[w] = (-1) * c
                    if not dfs(w, colors[w]):
                        return False
                elif colors[w] == c:
                    return False

            return True

        for i in range(n):
            if colors[i] == 0:
                if not dfs(i, 1):
                    return False
        return True

    def is_bipartite(self, graph):
        n = len(graph)
        color = [0] * n
        for i in range(n):
            if color[i] == 0:
                color[i] = 1
                q = deque()
                q.append(i)
                while q:
                    x = q.popleft()
                    for y in graph[x]:
                        if color[y] == color[x]:
                            return False
                        elif color[y] == 0:
                            color[y] = -color[x]
                            q.append(y)
        return True




if __name__ == '__main__':
    # graph = [[1], [0, 3], [3], [1, 2]]
    graph = [[3,4,6],[3,6],[3,6],[0,1,2,5],[0,7,8],[3],[0,1,2,7],[4,6],[4],[]]
    sol = Solution()
    res = sol.isBipartite(graph)
    print(res)
