# -*- coding : utf-8 -*-
# @Time: 2023/9/10 10:35
# @Author: yefei.wang
# @File: week-362.py

from typing import List
from itertools import permutations


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        mi = max(abs(sx - fx), abs(sy - fy))
        mx = abs(sx - fx) + abs(sy - fy)
        if mi == 0 and t == 1:
            return False
        if t < mi:
            return False
        return True

    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        start = []
        end = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 1:
                    for k in range(1, grid[i][j]):
                        start.append([i, j])
                elif grid[i][j] == 0:
                    end.append([i, j])

        def dis(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        ans = 18
        idxs = list(range(len(start)))
        for p in permutations(idxs):
            tmp = sum(dis(start[x][0], start[x][1], end[y][0], end[y][1]) for x, y in enumerate(p))
            ans = min(ans, tmp)
        return ans

    def numberOfWays(self, s: str, t: str, k: int) -> int:
        pass