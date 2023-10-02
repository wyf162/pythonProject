# _*_ coding: utf-8 _*_
# @Time : 2022/06/05 3:34 PM 
# @Author : yefe
# @File : 122_max_profit
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ret = 0
        for i in range(1, n):
            if prices[i]-prices[i+1]>0:
                ret += prices[i] - prices[i-1]
        return ret