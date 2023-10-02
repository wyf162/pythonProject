# -*- coding : utf-8 -*-
# @Time: 2022/7/3 19:03
# @Author: yefei.wang
# @File: 6110_count_paths.py
from functools import cache
from typing import List


class Solution:
    def countPaths2(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        nums = []
        for i in range(m):
            for j in range(n):
                nums.append((grid[i][j], i, j))
        nums.sort()

        dp = [[0 for j in range(n)] for i in range(m)]
        for k, x, y in nums:
            dp[x][y] = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]<grid[x][y]:
                    dp[x][y] += dp[nx][ny]
        # print(dp)
        return sum([sum(row) for row in dp]) % MOD

    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int) -> int:
            res = 1
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[i][j]:
                    res += dfs(x, y)
            return res % MOD
        return sum(dfs(i, j) for i in range(m) for j in range(n)) % MOD


if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 1], [3, 4]]
    ret = sol.countPaths(grid)
    print(ret)
