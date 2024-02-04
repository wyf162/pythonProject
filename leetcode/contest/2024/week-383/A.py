# -*- coding : utf-8 -*-
# @Time: 2024/2/4 10:29
# @Author: yefei.wang
# @File: A.py
from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        tot = 0
        ans = 0
        for x in nums:
            tot += x
            if tot == 0:
                ans += 1
        return ans