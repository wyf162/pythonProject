# -*- coding : utf-8 -*-
# @Time: 2022/1/22 23:20
# @Author: yefei.wang
# @File: 20220122.py
from typing import List
import functools


def my_compare(x, y):
    if x[2] < y[2]:
        return -1
    elif x[0] < y[0]:
        return -1
    elif x[1] < y[1]:
        return -1
    else:
        return 1


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        dp = [0]
        m, n = 0, 0
        for diff in differences:
            val = dp[-1] + diff
            m = min(m, val)
            n = max(n, val)
            dp.append(val)
        # print(m, n)
        ans = m - lower + 1 + upper - n
        return ans if ans > 0 else 0

    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[
        List[int]]:
        lower, upper = pricing
        m, n = len(grid), len(grid[0])
        visited = [[grid[i][j] == 0 for j in range(n)] for i in range(m)]

        def next_location_list(coord):
            res = list()
            x, y = coord
            if x - 1 >= 0 and not visited[x - 1][y]:
                res.append([x - 1, y])
                visited[x - 1][y] = True
            if x + 1 < m and not visited[x + 1][y]:
                res.append([x + 1, y])
                visited[x + 1][y] = True
            if y - 1 >= 0 and not visited[x][y - 1]:
                res.append([x, y - 1])
                visited[x][y - 1] = True
            if y + 1 < n and not visited[x][y + 1]:
                res.append([x, y + 1])
                visited[x][y + 1] = True
            return res

        ans = list()
        coords = [start]
        visited[start[0]][start[1]] = True
        while len(ans) < k and coords:
            tmp = [[x, y, grid[x][y]] for x, y in coords if lower <= grid[x][y] <= upper]
            tmp = sorted(tmp, key=functools.cmp_to_key(my_compare))
            new_tmp = [[x, y] for x, y, _ in tmp]
            ans.extend(new_tmp[0:k - len(ans)])
            new_coords = list()
            for coord in coords:
                new_coords.extend(next_location_list(coord))
            coords = new_coords
        return ans

    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        dp = [0] * n
        dp[0] = 0 if corridor[0] == 'P' else 1
        for i in range(1, n):
            dp[i] = dp[i - 1] + (0 if corridor[i] == 'P' else 1)
        print(dp)
        hst = dict()
        lower, upper = 0, dp[-1]
        for i in range(n):
            if 0 < dp[i] < upper and dp[i] % 2 == 0:
                hst[dp[i]] = hst.get(dp[i], 0) + 1
        print(hst)
        ans = 1
        MOD = 1000000007
        for k in hst.keys():
            ans = ans * hst[k] % MOD
        return ans


if __name__ == '__main__':
    sol = Solution()
    corridor = "SSPPSPS"
    # corridor = "PPSPSP"
    data = sol.numberOfWays(corridor)
    print(data)
    # grid = [[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]]
    # pricing = [2, 5]
    # start = [0, 0]
    # k = 3
    # grid = [[1, 2, 0, 1], [1, 3, 3, 1], [0, 2, 5, 1]]
    # pricing = [2, 3]
    # start = [2, 3]
    # k = 2
    # grid = [[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]]
    # pricing = [2, 5]
    # start = [0, 0]
    # k = 3
    # grid = [[1, 1, 1], [0, 0, 1], [2, 3, 4]]
    # pricing = [2, 3]
    # start = [0, 0]
    # k = 3
    # data = sol.highestRankedKItems(grid, pricing, start, k)
    # print(data)

    # differences = [3, -4, 5, 1, -2]
    # lower = -4
    # upper = 5
    # data = sol.numberOfArrays(differences, lower, upper)
    # print(data)
