# -*- coding : utf-8 -*-
# @Time: 2024/6/23 10:29
# @Author: yefei.wang
# @File: B.py

from typing import List


class Solution:
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
        ret = (x2 - x1) * (y2 - y1)
        return ret


