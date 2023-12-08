# -*- coding : utf-8 -*-
# @Time: 2023/12/3 10:28
# @Author: yefei.wang
# @File: A.py
from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        peak = []
        for i in range(1, n-1):
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                peak.append(i)
        return peak