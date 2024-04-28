# -*- coding : utf-8 -*-
# @Time: 2024/4/28 10:31
# @Author: yefei.wang
# @File: A.py

from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        return nums2[0] - nums1[0]
