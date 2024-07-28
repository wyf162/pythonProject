# -*- coding : utf-8 -*-
# @Time: 2024/7/28 10:26
# @Author: yefei.wang
# @File: A.py

from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        tot1, tot2 = 0, 0
        for x in nums:
            if x < 10:
                tot1 += x
            else:
                tot2 += x
        return tot1 != tot2
