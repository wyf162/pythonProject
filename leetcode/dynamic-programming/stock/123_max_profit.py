# _*_ coding: utf-8 _*_
# @Time : 2022/06/05 3:36 PM 
# @Author : yefe
# @File : 123_max_profit
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1+prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2+prices[i])
        return sell2