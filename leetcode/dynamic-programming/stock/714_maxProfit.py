# -*- coding : utf-8 -*-
# @Time: 2023/10/6 14:26
# @Author: yefei.wang
# @File: 714_maxProfit.py

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]
