# _*_ coding: utf-8 _*_
# @Time : 2022/4/29 7:36 PM
# @Author : yefe
# @File : 427_construct
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(grid):
            root = Node(None, None, None, None, None, None)
            if self.check(grid):
                root.isLeaf = True
                root.val = grid[0][0]
            else:
                root.isLeaf = False
                root.val = grid[0][0]
                tl, tr, bl, br = self.split(grid)
                root.topLeft = dfs(tl)
                root.topRight = dfs(tr)
                root.bottomLeft = dfs(bl)
                root.bottomRight = dfs(br)
            return root

        ret = dfs(grid)
        return ret

    @staticmethod
    def check(grid):
        val = grid[0][0]
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == val:
                    continue
                return False
        return True

    @staticmethod
    def split(grid):
        n = len(grid)
        m = n >> 1
        tl = []
        for i in range(m):
            tmp = []
            for j in range(m):
                tmp.append(grid[i][j])
            tl.append(tmp)
        tr = []
        for i in range(m):
            tmp = []
            for j in range(m, n):
                tmp.append(grid[i][j])
            tr.append(tmp)
        bl = []
        for i in range(m, n):
            tmp = []
            for j in range(m):
                tmp.append(grid[i][j])
            bl.append(tmp)
        br = []
        for i in range(m, n):
            tmp = []
            for j in range(m, n):
                tmp.append(grid[i][j])
            br.append(tmp)
        return tl, tr, bl, br


if __name__ == '__main__':
    grid = [[0,1],[1,0]]
    sol = Solution()
    ret = sol.construct(grid)
    print(ret.val)