# -*- coding : utf-8 -*-
# @Time: 2024/5/19 10:30
# @Author: yefei.wang
# @File: A.py

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] % 2 == 0 and nums[i] % 2 == 0:
                return False
            if nums[i-1] % 2 == 1 and nums[i] % 2 == 1:
                return False
        return True
