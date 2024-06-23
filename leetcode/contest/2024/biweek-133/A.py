# -*- coding : utf-8 -*-
# @Time: 2024/6/22 22:29
# @Author: yefei.wang
# @File: A.py

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if x % 3 != 0:
                ans += 1
        return ans
