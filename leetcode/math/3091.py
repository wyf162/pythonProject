# -*- coding: utf-8 -*-
# @Time: 2024/3/25 15:08
# @Author: yfwang
# @File: 3091.py

class Solution:
    def minOperations(self, k: int) -> int:
        ans = k - 1
        for x in range(2, k):
            ans = min(ans, x - 1 + (k + x - 1) // x)
        return ans
