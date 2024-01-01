# -*- coding : utf-8 -*-
# @Time: 2023/12/10 10:30
# @Author: yefei.wang
# @File: A.py

from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for x in batteryPercentages:
            if x > ans:
                ans += 1
        return ans
