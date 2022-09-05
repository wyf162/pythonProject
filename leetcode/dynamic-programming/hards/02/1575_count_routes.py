# _*_ coding: utf-8 _*_
# @Time : 2022/09/03 1:17 PM 
# @Author : yefe
# @File : 1575_count_routes

from typing import List


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 9**10+7
        m = fuel
        n = len(locations)
        dists = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dists[i][j] = abs(locations[i] - locations[j])

        f = [[0] * n for _ in range(m + 1)]

        f[0][start] = 1

        for i in range(m + 1):
            for j in range(n):
                for k in range(n):
                    if j==k:
                        continue
                    if i + dists[j][k] <= m:
                        f[i + dists[j][k]][k] += f[i][j]

        ans = 0
        for i in range(m+1):
            ans += f[i][finish]
        ans %= MOD

        return ans


if __name__ == '__main__':
    sol = Solution()
    locations = [2, 3, 6, 8, 4]
    start = 1
    finish = 3
    fuel = 5
    ret = sol.countRoutes(locations, start, finish, fuel)
    print(ret)
