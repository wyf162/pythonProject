# -*- coding : utf-8 -*-
# @Time: 2024/8/4 10:29
# @Author: yefei.wang
# @File: A.py

from typing import List


class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.hst = dict()
        self.n = len(self.grid)
        for i in range(self.n):
            for j in range(self.n):
                self.hst[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        i, j = self.hst[value]
        ret = 0
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = i + dx, j + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                ret += self.grid[nx][ny]
        return ret

    def diagonalSum(self, value: int) -> int:
        i, j = self.hst[value]
        ret = 0
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = i + dx, j + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                ret += self.grid[nx][ny]
        return ret
