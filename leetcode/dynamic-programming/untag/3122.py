# -*- coding: utf-8 -*-
# @Time: 2024/4/25 17:19
# @Author: yfwang
# @File: 3122.py

from functools import cache
from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = [[0] * 10 for _ in range(n)]
        for row in grid:
            for j, x in enumerate(row):
                cnt[j][x] += 1

        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0
            return max(dfs(i - 1, k) + c for k, c in enumerate(cnt[i]) if k != j)

        return m * n - dfs(n - 1, 10)
