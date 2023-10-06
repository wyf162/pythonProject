# -*- coding : utf-8 -*-
# @Time: 2023/10/3 17:03
# @Author: yefei.wang
# @File: 123_maxProfit.py
from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        f = [[-inf] * 2 for _ in range(k + 2)]
        for j in range(1, k + 2):
            f[j][0] = 0
        for i, p in enumerate(prices):
            for j in range(k + 1, 0, -1):
                f[j][0] = max(f[j][0], f[j][1] + p)
                f[j][1] = max(f[j][1], f[j - 1][0] - p)
        return f[-1][0]
