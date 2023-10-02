# -*- coding : utf-8 -*-
# @Time: 2023/9/29 13:27
# @Author: yefei.wang
# @File: 1368_minCost.py

from typing import List
from collections import deque


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[False for j in range(n)] for i in range(m)]
        q = deque()
        q.append((0, 0, 0))
        while q:
            c, i, j = q.popleft()
            if vis[i][j]:
                continue
            vis[i][j] = True
            if i == m - 1 and j == n - 1:
                return c
            if j + 1 < n and not vis[i][j + 1]:
                if grid[i][j] == 1:
                    q.appendleft((c, i, j + 1))
                else:
                    q.append((c + 1, i, j + 1))

            if j - 1 >= 0 and not vis[i][j - 1]:
                if grid[i][j] == 2:
                    q.appendleft((c, i, j - 1))
                else:
                    q.append((c + 1, i, j - 1))

            if i + 1 < m and not vis[i + 1][j]:
                if grid[i][j] == 3:
                    q.appendleft((c, i + 1, j))
                else:
                    q.append((c + 1, i + 1, j))

            if i - 1 >= 0 and not vis[i - 1][j]:
                if grid[i][j] == 4:
                    q.appendleft((c, i - 1, j))
                else:
                    q.append((c + 1, i - 1, j))


if __name__ == '__main__':
    sol = Solution()
    grid = [[2, 2, 2], [2, 2, 2]]
    ret = sol.minCost(grid)
    print(ret)
