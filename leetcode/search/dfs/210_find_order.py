# _*_ coding: utf-8 _*_
# @Time : 2022/08/20 1:26 PM 
# @Author : yefe
# @File : 210_find_order
from typing import List


class Solution:
    def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:

        g = [[] for _ in range(n)]
        for v, u in edges:
            g[u].append(v)

        # 0, 1, 2
        visited = [0]*n
        stk = []
        valid = True

        def dfs(x: int):
            nonlocal valid
            visited[x] = 1
            for y in g[x]:
                if visited[y] == 0:
                    dfs(y)
                    if not valid:
                        return
                elif visited[y] == 1:
                    valid = False
                    return
            visited[x] = 2
            stk.append(x)

        for i in range(n):
            if valid and not visited[i]:
                dfs(i)

        if not valid:
            return []
        else:
            return stk[::-1]


if __name__ == '__main__':
    sol = Solution()
    n = 2
    edges = [[1,0]]
    ret = sol.findOrder(n, edges)
    print(ret)
