# -*- coding: utf-8 -*-
# @Time: 2024/5/13 15:01
# @Author: yfwang
# @File: 3148.py

from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        inf = 0x3f3f3f3f
        dp = [[inf for _ in range(n + 1)] for _ in range(m + 1)]
        ans = -inf
        for i in range(m):
            for j in range(n):
                ans = max(ans, grid[i][j] - dp[i][j + 1], grid[i][j] - dp[i + 1][j])
                dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], grid[i][j])
        return ans


if __name__ == '__main__':
    sol = Solution()
    # grid = [[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]]
    grid = [[4, 3, 2], [3, 2, 1]]
    ret = sol.maxScore(grid)
    print(ret)
