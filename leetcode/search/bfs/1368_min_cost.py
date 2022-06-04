# _*_ coding: utf-8 _*_
# @Time : 2022/06/04 7:57 PM 
# @Author : yefe
# @File : 1368_min_cost
import heapq
from typing import List
import collections


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MAX = 10 ** 9
        dist = [0] + [MAX] * (m * n - 1)
        seen = set()
        q = collections.deque([(0, 0)])
        while len(q) > 0:
            x, y = q.popleft()
            if (x, y) in seen:
                continue
            seen.add((x, y))
            cur_pos = x * n + y
            for i, (nx, ny) in enumerate([(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]):
                new_pos = nx * n + ny
                new_dis = dist[cur_pos] + (1 if grid[x][y] != i + 1 else 0)
                if 0 <= nx < m and 0 <= ny < n and new_dis < dist[new_pos]:
                    dist[new_pos] = new_dis
                    if grid[x][y] == i + 1:
                        q.appendleft((nx, ny))
                    else:
                        q.append((nx, ny))
        return dist[m * n - 1]

    def min_cost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MAX = 10 ** 9
        dist = [[MAX for j in range(n)] for i in range(m)]
        dist[0][0] = 0

        seen = set()
        q = [(0, 0, 0)]

        while q:
            cur_dis, x, y = heapq.heappop(q)
            if (x, y) in seen:
                continue
            seen.add((x, y))
            for i, (nx, ny) in enumerate([(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]):
                new_dis = dist[x][y] + (1 if grid[x][y] != i + 1 else 0)
                if 0 <= nx < m and 0 <= ny < n and new_dis < dist[nx][ny]:
                    dist[nx][ny] = new_dis
                    heapq.heappush(q, (new_dis, nx, ny))

        return dist[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
    ret = sol.min_cost(grid)
    print(ret)
