# _*_ coding: utf-8 _*_
# @Time : 2022/06/04 7:43 PM 
# @Author : yefe
# @File : 200_num_islands
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    q = [(i, j)]
                    grid[i][j] = '2'
                    while q:
                        x, y = q.pop()
                        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                                q.append((nx, ny))
                                grid[nx][ny] = '2'
        return cnt


if __name__ == '__main__':
    sol = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    ret = sol.numIslands(grid)
    print(ret)
