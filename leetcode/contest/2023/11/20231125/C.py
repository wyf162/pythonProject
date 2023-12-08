# -*- coding : utf-8 -*-
# @Time: 2023/11/25 22:28
# @Author: yefei.wang
# @File: C.py

from typing import List


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [10 ** 9] * (3 * n)
        dp[0] = 0
        for i, price in enumerate(prices, start=1):
            dp[i] = min(dp[i], dp[i - 1] + price)
            for j in range(i + i, i, -1):
                dp[j] = min(dp[j], dp[i - 1] + price)
        rst = min(dp[n:])
        return rst


if __name__ == '__main__':
    sol = Solution()
    prices = [3, 1, 2]
    # prices = [1, 10, 1, 1]
    ret = sol.minimumCoins(prices)
    print(ret)
