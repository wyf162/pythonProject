# -*- coding : utf-8 -*-
# @Time: 2023/12/17 10:30
# @Author: yefei.wang
# @File: A.py
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        a = [0 for i in range(n * n + 1)]
        for i in range(n):
            for j in range(n):
                x = grid[i][j]
                a[x] += 1
        rst = [0, 0]
        for i in range(1, n*n+1, 1):
            if a[i] == 0:
                rst[1] = i
            elif a[i] == 1:
                rst[0] = i
        return rst
