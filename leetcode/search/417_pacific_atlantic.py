# _*_ coding: utf-8 _*_
# @Time : 2022//27 10:36 AM 
# @Author : yefe
# @File : 417_pacific_atlantic
from collections import deque
from typing import List, Tuple, Set


class SolutionSelf:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dp_p = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            dp_p[i][0] = 1
        for j in range(n):
            dp_p[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if heights[i][j] >= heights[i - 1][j] or heights[i][j] >= heights[i][j-1]:
                    dp_p[i][j] = max(dp_p[i - 1][j], dp_p[i][j - 1])

        # atlantic
        dp_a = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            dp_a[i][-1] = 1
        for j in range(n):
            dp_a[-1][j] = 1
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if heights[i][j] >= heights[i + 1][j] or heights[i][j] >= heights[i + 1][j]:
                    dp_a[i][j] = max(dp_a[i + 1][j], dp_a[i][j + 1])

        ret = list()
        for i in range(m):
            for j in range(n):
                if dp_p[i][j] and dp_a[i][j]:
                    ret.append([i, j])
        return ret


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def bfs(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            q = deque(starts)
            visited = set(starts)
            while q:
                x, y = q.popleft()
                for nx, ny in ((x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)):
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))
            return visited

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)]
        return list(map(list, bfs(pacific) & bfs(atlantic)))


if __name__ == '__main__':
    sol = Solution()
    # heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    heights = [[1,2,3],[8,9,4],[7,6,5]]
    ret = sol.pacificAtlantic(heights)
    print(ret)
