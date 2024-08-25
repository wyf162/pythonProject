# -*- coding : utf-8 -*-
# @Time: 2024/8/25 10:30
# @Author: yefei.wang
# @File: A.py

from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            i = nums.index(min(nums))
            nums[i] *= multiplier
        return nums


