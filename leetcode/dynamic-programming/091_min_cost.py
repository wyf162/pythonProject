# -*- coding : utf-8 -*-
# @Time: 2022/6/25 0:08
# @Author: yefei.wang
# @File: 091_min_cost.py
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0] = costs[0]
        for i, cost in enumerate(costs):
            if i == 0:
                continue
            for j in range(3):
                for k in range(3):
                    if j == k:
                        continue
                    else:
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + cost[j])
            print(dp[i])

        return min(dp[-1])


if __name__ == '__main__':
    sol = Solution()
    # costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    costs = [[3,5,3],[6,17,6],[7,13,18],[9,10,18]]
    ret = sol.minCost(costs)
    print(ret)
