# -*- coding : utf-8 -*-
# @Time: 2024/6/23 10:29
# @Author: yefei.wang
# @File: A.py

from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        nums.sort()
        averages = []
        for i in range(n//2):
            x1, x2 = nums[i], nums[n - 1 - i]
            averages.append((x1 + x2) / 2)
        return min(averages)