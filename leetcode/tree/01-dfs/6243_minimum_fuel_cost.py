# _*_ coding: utf-8 _*_
# @Time : 2022/11/20 2:33 PM 
# @Author : yefe
# @File : 6243_minimum_fuel_cost

from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        ans = 0
        g = [[] for _ in range(len(roads) + 1)]
        for x, y in roads:
            g[x].append(y)
            g[y].append(x)

        def dfs(x: int, fa: int) -> int:
            size = 1
            for y in g[x]:
                if y != fa:
                    size += dfs(y, x)
            if x:
                nonlocal ans
                ans += (size + seats - 1) // seats
            return size
        dfs(0, -1)
        return ans

