# -*- coding: utf-8 -*-
# @Time: 2024/7/22 16:17
# @Author: yfwang
# @File: 3225.py

from typing import List


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in grid:
            ans += sum(row) - min(row)
        return ans


if __name__ == '__main__':
    sol = Solution()
    grid = [[0, 0, 0, 0, 0], [0, 0, 3, 0, 0], [0, 1, 0, 0, 0], [5, 0, 0, 3, 0], [0, 0, 0, 0, 2]]
    ret = sol.maximumScore(grid)
    print(ret)