# -*- coding : utf-8 -*-
# @Time: 2021/12/7 21:41
# @Author: yefei.wang
# @File: 1034_colorBorder.py

from typing import List
import copy
import collections

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        unvisited = [[True for j in range(n)] for i in range(m)]
        ans = copy.deepcopy(grid)
        dq = collections.deque()
        dq.append([row,col])
        k = grid[row][col]
        while dq:
            tag = 0
            row,col = dq.popleft()
            print(dq)
            if col-1>-1 and grid[row][col-1]==k:
                if unvisited[row][col-1]:
                    dq.append([row,col-1])
                    unvisited[row][col-1]=False
                tag += 1
            if col+1<n and grid[row][col+1]==k:
                if unvisited[row][col+1]:
                    dq.append([row,col+1])
                    unvisited[row][col+1]=False
                tag += 1
            if row-1>-1 and grid[row-1][col]==k:
                if unvisited[row-1][col]:
                    dq.append([row-1,col])
                    unvisited[row-1][col]=False
                tag +=1
            if row+1<m and grid[row+1][col]==k:
                if  unvisited[row+1][col]:
                    dq.append([row+1,col])
                    unvisited[row+1][col]=False
                tag += 1
            if tag<4:
                ans[row][col]=color
        print(ans)
        return ans


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 1], [1, 2]]
    row = 0
    col = 0
    color = 3
    sol.colorBorder(grid,row,col,color)