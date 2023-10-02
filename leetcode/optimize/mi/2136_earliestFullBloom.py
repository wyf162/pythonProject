# -*- coding : utf-8 -*-
# @Time: 2023/9/30 12:36
# @Author: yefei.wang
# @File: 2136_earliestFullBloom.py

from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        a = list(zip(plantTime, growTime))
        a.sort(key=lambda x:-x[1])
        ans, day = 0, 0
        for p in a:
            day += p[0]
            ans = max(ans, day + p[1])
        return ans
