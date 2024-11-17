# -*- coding : utf-8 -*-
# @Time: 2024/8/3 22:40
# @Author: yefei.wang
# @File: C.py

from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ret = 0
        for i in range(n // 2):
            for j in range(m // 2):
                i1, j1 = i, j
                i2, j2 = n - 1 - i, j
                i3, j3 = i, m - 1 - j
                i4, j4 = n - 1 - i, m - 1 - j
                c = grid[i1][j1] + grid[i2][j2] + grid[i3][j3] + grid[i4][j4]
                ret += min(c, 4 - c)

        c1 = 0
        c2 = 0

        if n % 2:
            for j in range(m // 2):
                if grid[n // 2][j] + grid[n // 2][m - 1 - j] == 2:
                    c1 += 1
                if grid[n // 2][j] + grid[n // 2][m - 1 - j] == 1:
                    ret += 1
                    c2 += 1
        if m % 2:
            for i in range(n // 2):
                if grid[i][m // 2] + grid[n - 1 - i][m // 2] == 2:
                    c1 += 1
                if grid[i][m // 2] + grid[n - 1 - i][m // 2] == 1:
                    ret += 1
                    c2 += 1
        if n % 2 and m % 2:
            ret += grid[n // 2][m // 2]

        if c1 % 2 and c2 == 0:
            ret += 2

        return ret


if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
    ret = sol.minFlips(grid)
    print(ret)
