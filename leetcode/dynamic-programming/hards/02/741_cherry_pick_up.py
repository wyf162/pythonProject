# _*_ coding: utf-8 _*_
# @Time : 2022/09/03 5:11 PM 
# @Author : yefe
# @File : 741_cherry_pick_up

from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        n = len(grid)
        for j in range(1, n):
            if grid[0][j] == -1:
                break
            else:
                grid[0][j] += grid[0][j - 1]

        for i in range(1, n):
            if grid[i][0] == -1:
                break
            else:
                grid[i][0] += grid[i - 1][0]

        for i in range(1, n):
            for j in range(1, n):
                if grid[i - 1][j] == -1 and grid[i][j - 1] == -1:
                    return 0
                elif grid[i - 1][j] == -1:
                    grid[i][j] += grid[i][j - 1]
                elif grid[i][j - 1] == -1:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i-1][j-1]

        return grid[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    grid = [[0, 1, -1],
            [1, 0, -1],
            [1, 1, 1]]
    ret = sol.cherryPickup(grid)
    print(ret)
