# _*_ coding: utf-8 _*_
# @Time : 2022/05/02 10:10 PM 
# @Author : yefe
# @File : 16019_pond_sizes
from typing import List


class Solution:

    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m = len(land)
        n = len(land[0])

        def bfs(loc):
            q = [loc]
            ret = 0
            nonlocal land
            while q:
                x, y = q.pop()
                ret += 1
                for dx, dy in zip([-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and land[nx][ny] == 0:
                        land[nx][ny] = -1
                        q.append((nx, ny))
            return ret

        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    land[i][j] = -1
                    res.append(bfs((i, j)))
        res.sort()
        return res


if __name__ == '__main__':
    sol = Solution()
    land = [
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ]
    res = sol.pondSizes(land)
    print(res)
