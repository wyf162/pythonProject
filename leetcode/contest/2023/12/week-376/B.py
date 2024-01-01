# -*- coding : utf-8 -*-
# @Time: 2023/12/17 10:34
# @Author: yefei.wang
# @File: B.py

from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ret = []
        for i in range(3, n, 3):
            if nums[i-1] - nums[i-3] <= k:
                ret.append(nums[i-3:i])
            else:
                return []
        return ret
