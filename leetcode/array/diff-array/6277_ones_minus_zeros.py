# _*_ coding: utf-8 _*_
# @Time : 2022/11/27 2:10 PM 
# @Author : yefe
# @File : 6277_ones_minus_zeros

from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = [0]*m
        cols = [0]*n

        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]

        diff = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                diff[i][j] = 2*(rows[i]+cols[j]) - (m+n)
        return diff
