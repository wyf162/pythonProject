# -*- coding : utf-8 -*-
# @Time: 2024/7/7 10:21
# @Author: yefei.wang
# @File: C.py

from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        grid_X = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        grid_Y = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                grid_X[i + 1][j + 1] = grid_X[i + 1][j] + grid_X[i][j + 1] - grid_X[i][j] + int(grid[i][j] == 'X')
                grid_Y[i + 1][j + 1] = grid_Y[i + 1][j] + grid_Y[i][j + 1] - grid_Y[i][j] + int(grid[i][j] == 'Y')

        ans = 0
        for i in range(n):
            for j in range(m):
                cnt_X = grid_X[i + 1][j + 1]
                cnt_Y = grid_Y[i + 1][j + 1]
                if cnt_X == cnt_Y > 0:
                    ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    # grid = [["X", "Y", "."], ["Y", ".", "."]]
    # grid = [["X", "X"], ["X", "Y"]]
    grid = [[".", "."], [".", "."]]
    ret = sol.numberOfSubmatrices(grid)
    print(ret)
