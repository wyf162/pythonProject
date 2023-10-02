# _*_ coding: utf-8 _*_
# @Time : 2022/08/25 9:19 PM 
# @Author : yefe
# @File : 1595_connect_two_groups

from typing import List
import math


class Solution:

    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        M = 0x3f3f3f3f
        m = len(cost)
        n = len(cost[0])
        dp = [[M for j in range(1 << n)] for i in range(1 << m)]
        dp[0][0] = 0
        for i in range(1 << m):
            for j in range(1 << n):
                if dp[i][j] == M:
                    continue
                for a in range(m):
                    for b in range(n):
                        dp[i | (1 << a)][j | (1 << b)] = min(dp[i | (1 << a)][j | (1 << b)], dp[i][j] + cost[a][b])
        return dp[(1 << m) - 1][(1 << n) - 1]


if __name__ == '__main__':
    sol = Solution()
    cost = [[15, 96], [36, 2]]
    ret = sol.connectTwoGroups(cost)
    print(ret)

    # cnt = math.factorial(12)
    # print(cnt)
