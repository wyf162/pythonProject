# -*- coding : utf-8 -*-
# @Time: 2024/4/7 10:29
# @Author: yefei.wang
# @File: A.py

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        n = len(nums)
        tmp = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                tmp += 1
            else:
                ans = max(ans, tmp)
                tmp = 1
        ans = max(ans, tmp)
        tmp = 1
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                tmp += 1
            else:
                ans = max(ans, tmp)
                tmp = 1
        ans = max(ans, tmp)
        return ans
