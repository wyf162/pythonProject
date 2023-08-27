# _*_ coding: utf-8 _*_
# @Time : 2022/08/13 4:33 PM 
# @Author : yefe
# @File : 778_swim_in_water
from typing import List
from collections import defaultdict


class UnionFind:

    def __init__(self, n):
        self.parent = [_ for _ in range(n)]

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x < root_y:
            self.parent[root_y] = root_x
            return root_x
        else:
            self.parent[root_x] = root_y
            return root_y

    def are_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        hst = defaultdict(list)
        for i in range(n):
            for j in range(n):
                hst[grid[i][j]].append([i, j])

        uf = UnionFind(n * n)

        for t in range(n * n):
            for x, y in hst[t]:
                for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny]<=t:
                        uf.merge(x * n + y, nx * n + ny)
            if uf.are_connected(0, n*n-1):
                return t


if __name__ == '__main__':
    sol = Solution()
    grid = [[0, 2], [1, 3]]
    ret = sol.swimInWater(grid)
    print(ret)
