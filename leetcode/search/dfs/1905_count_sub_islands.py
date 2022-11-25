# _*_ coding: utf-8 _*_
# @Time : 2022/11/20 9:33 PM 
# @Author : yefe
# @File : 1905_count_sub_islands

from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i: int, j: int):
            if i < 0 or i >= len(grid1) or j < 0 or j >= len(grid1[0]) or grid2[i][j] == 0:
                return
            if grid1[i][j] == 0:
                nonlocal flag
                flag = False
                return
            grid2[i][j] = 0
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                dfs(i + dx, i + dy)

        ans = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1:
                    flag = True
                    dfs(i, j)
                    ans += int(flag)
        return ans


if __name__ == '__main__':
    sol = Solution()
    grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
    grid2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
    ret = sol.countSubIslands(grid1, grid2)
    print(ret)
