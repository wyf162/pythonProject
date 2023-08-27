# _*_ coding: utf-8 _*_
# @Time : 2022/08/18 9:11 PM 
# @Author : yefe
# @File : 1568_minDays
from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x: int, y: int):
            grid[x][y] = 2
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tx, ty = x + dx, y + dy
                if 0 <= tx < m and 0 <= ty < m and grid[tx][ty] == 1:
                    dfs(tx, ty)

        def count():
            cnt = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        cnt += 1
                        dfs(i, j)
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        grid[i][j] = 1
            return cnt

        if count() != 1:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count() != 1:
                        return 1
                    grid[i][j] = 1

        return 2
