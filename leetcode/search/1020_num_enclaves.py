# -*- coding : utf-8 -*-
# @Time: 2022/2/12 13:26
# @Author: yefei.wang
# @File: 1020_num_enclaves.py
import collections
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        unvisted = [[True for j in range(n)] for i in range(m)]
        dq = collections.deque()
        for i in range(m):
            for k in [0, n - 1]:
                if grid[i][k] == 1 and unvisted[i][k]:
                    dq.append([i, k])
                    unvisted[i][k] = False
        for j in range(n):
            for k in [0, m - 1]:
                if grid[k][j] == 1 and unvisted[k][j]:
                    dq.append([k, j])
                    unvisted[k][j] = False
        cnt = 0
        while dq:
            x, y = dq.popleft()
            cnt += 1
            for d_x, d_y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                n_x, n_y = x + d_x, y + d_y
                if 0 <= n_x < m and 0 <= n_y < n and grid[n_x][n_y] == 1 and unvisted[n_x][n_y]:
                    dq.append([n_x, n_y])
                    unvisted[n_x][n_y] = False
        ones = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ones += 1
        return ones - cnt


if __name__ == '__main__':
    sol = Solution()
    grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    ans = sol.numEnclaves(grid)
