# -*- coding : utf-8 -*-
# @Time: 2024/6/23 10:46
# @Author: yefei.wang
# @File: D.py

from typing import List


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = n * m
        for i in range(n - 1):
            grid1 = [grid[i1][:] for i1 in range(i + 1)]
            ret1 = self.minimumArea(grid1)
            for j in range(m - 1):
                grid2 = [grid[i1][:j + 1] for i1 in range(i + 1, n)]
                grid3 = [grid[i1][j + 1:m] for i1 in range(i + 1, n)]
                # print(grid1, grid2, grid3)
                ret2 = self.minimumArea(grid2)
                ret3 = self.minimumArea(grid3)
                ans = min(ans, ret1 + ret2 + ret3)

        for i in range(n - 1):
            grid1 = [grid[i1][:] for i1 in range(i + 1, n)]
            ret1 = self.minimumArea(grid1)
            for j in range(m - 1):
                grid2 = [grid[i1][:j + 1] for i1 in range(i + 1)]
                grid3 = [grid[i1][j + 1:m] for i1 in range(i + 1)]
                # print(grid1, grid2, grid3)
                ret2 = self.minimumArea(grid2)
                ret3 = self.minimumArea(grid3)
                ans = min(ans, ret1 + ret2 + ret3)

        for j in range(m - 1):
            grid1 = [grid[i1][:j + 1] for i1 in range(n)]
            ret1 = self.minimumArea(grid1)
            for i in range(n - 1):
                grid2 = [grid[i1][j + 1:] for i1 in range(i + 1)]
                grid3 = [grid[i1][j + 1:] for i1 in range(i + 1, n)]
                # print(grid1, grid2, grid3)
                ret2 = self.minimumArea(grid2)
                ret3 = self.minimumArea(grid3)
                ans = min(ans, ret1 + ret2 + ret3)

        for j in range(m - 1):
            grid1 = [grid[i1][j + 1:] for i1 in range(n)]
            ret1 = self.minimumArea(grid1)
            for i in range(n - 1):
                grid2 = [grid[i1][:j + 1] for i1 in range(i + 1)]
                grid3 = [grid[i1][:j + 1] for i1 in range(i + 1, n)]
                # print(grid1, grid2, grid3)
                ret2 = self.minimumArea(grid2)
                ret3 = self.minimumArea(grid3)
                ans = min(ans, ret1 + ret2 + ret3)

        for i in range(n - 1):
            grid1 = [grid[i1][:] for i1 in range(i + 1)]
            ret1 = self.minimumArea(grid1)
            for k in range(i + 1, n - 1):
                grid2 = [grid[i1][:] for i1 in range(i + 1, k+1)]
                grid3 = [grid[i1][:] for i1 in range(k + 1, n)]
                # print(grid1, grid2, grid3)
                ret2 = self.minimumArea(grid2)
                ret3 = self.minimumArea(grid3)
                ans = min(ans, ret1 + ret2 + ret3)

        for j in range(m - 1):
            grid1 = [grid[i1][:j+1] for i1 in range(n)]
            ret1 = self.minimumArea(grid1)
            for k in range(j + 1, m - 1):
                grid2 = [grid[i1][j+1:k+1] for i1 in range(n)]
                grid3 = [grid[i1][k+1:] for i1 in range(n)]
                # print(grid1, grid2, grid3)
                ret2 = self.minimumArea(grid2)
                ret3 = self.minimumArea(grid3)
                ans = min(ans, ret1 + ret2 + ret3)

        return ans

    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        x1, x2 = n, 0
        y1, y2 = m, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    x1 = min(x1, i)
                    x2 = max(x2, i)
                    y1 = min(y1, j)
                    y2 = max(y2, j)
        ret = (x2 - x1 + 1) * (y2 - y1 + 1)
        return ret


if __name__ == '__main__':
    sol = Solution()
    # grid = [[1, 0, 1], [1, 1, 1]]
    # grid = [[1, 0, 1, 0], [0, 1, 0, 1]]
    # grid = [[0, 0, 0], [0, 0, 1], [0, 0, 0], [1, 0, 1]]
    grid = [[0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    ret = sol.minimumSum(grid)
    print(ret)
