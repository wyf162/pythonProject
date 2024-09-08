# -*- coding : utf-8 -*-
# @Time: 2024/9/8 10:41
# @Author: yefei.wang
# @File: C.py

from typing import List


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        mx = [nums[0]]
        for i in range(1, n):
            mx.append(max(mx[-1], nums[i]))
        ret = sum(mx[:-1])
        return ret
