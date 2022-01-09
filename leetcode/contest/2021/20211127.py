# _*_ coding: utf-8 _*_
# @Time : 2021/11/27 下午10:48 
# @Author : wangyefei
# @File : 20211127.py
from typing import List


class Solution:
    def minimumBuckets(self, street: str) -> int:
        bucket = 0
        street = list(street)
        for idx, s in enumerate(street):
            if s == 'H':
                if idx - 1 >= 0 and street[idx - 1] == 'B':
                    continue
                elif idx + 1 < len(street) and street[idx + 1] == '.':
                    bucket += 1
                    street[idx + 1] = 'B'
                elif idx - 1 >= 0 and street[idx - 1] == ".":
                    bucket += 1
                    street[idx - 1] = 'B'
                else:
                    return -1
        return bucket

    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ans = 0
        s, t = startPos[0], homePos[0]
        if s < t:
            for i in range(s + 1, t + 1):
                ans += rowCosts[i]
        else:
            for i in range(s - 1, t - 1, -1):
                ans += rowCosts[i]

        s, t = startPos[1], homePos[1]
        if s < t:
            for i in range(s + 1, t + 1):
                ans += colCosts[i]
        else:
            for i in range(s - 1, t - 1, -1):
                ans += colCosts[i]
        return ans

    def countPyramids(self, grid: List[List[int]]) -> int:
        self.down = 0
        self.up = 0
        m, n = len(grid), len(grid[0])
        hst = dict()
        hst[1] = 0
        hst[2] = 1
        t = 4
        for i in range(3, min(m, n) + 1):
            hst[i] = hst[i - 1] + t
            t = t + 2 * i - 3
        print(hst)
        visited = [[0 for j in range(n)] for i in range(m)]

        def dfs(coord, h, d='down'):
            x, y = coord
            if d == 'down':
                if x + 1 < m and y - h >= 0 and y + h < n:
                    tag = True
                    for j in range(y - h, y + h + 1):
                        if grid[x+1][j] == 0:
                            tag = False
                            break
                    if tag:
                        for j in range(y - h, y + h + 1):
                            visited[x + 1][j] = 1
                        dfs([x + 1, y], h + 1, d='down')
                else:
                    self.down += hst[h]
            else:
                if x - 1 >= 0 and y - h >= 0 and y + h < n:
                    tag = True
                    for j in range(y - h, y + h + 1):
                        if grid[x-1][j] == 0:
                            tag = False
                            break
                    if tag:
                        for j in range(y - h, y + h + 1):
                            visited[x - 1][j] = 1
                        dfs([x - 1, y], h + 1, d='up')
                else:
                    self.up += hst[h]

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    dfs([i, j], 1, d='down')
        print(self.down)
        visited = [[0 for j in range(n)] for i in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if not visited[i][j]:
                    dfs([i, j], 1, d='up')
        print(self.up)
        return self.down+self.up


if __name__ == "__main__":
    sol = Solution()
    # grid = [[0, 1, 1, 0], [1, 1, 1, 1]]
    grid = [[1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 0, 0, 1]]
    print(sol.countPyramids(grid))

    # start_pos = [2,3]
    # home_pos = [2,3]
    # row_costs = [5,4,3]
    # col_costs = [8,2,6,7]
    # print(sol.minCost(start_pos, home_pos, row_costs, col_costs))
    # print(sol.minCost(home_pos, start_pos, row_costs, col_costs))

    # street = "H..H"
    # print(sol.minimumBuckets(street))
