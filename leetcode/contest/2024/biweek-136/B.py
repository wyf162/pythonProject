# -*- coding : utf-8 -*-
# @Time: 2024/8/3 22:35
# @Author: yefei.wang
# @File: B.py

from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ret1 = 0
        for i in range(n):
            for j in range(m // 2):
                ret1 += grid[i][j] ^ grid[i][m - 1 - j]

        ret2 = 0
        for i in range(n//2):
            for j in range(m):
                ret2 += grid[i][j] ^ grid[n-1-i][j]

        ret = min(ret1, ret2)
        return ret


if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
    ret = sol.minFlips(grid)
    print(ret)
