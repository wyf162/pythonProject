# -*- coding : utf-8 -*-
# @Time: 2023/12/9 22:30
# @Author: yefei.wang
# @File: A.py

from typing import List
from collections import Counter


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        n1, n2 = 0, 0
        for k, v in cnt1.items():
            if k in cnt2:
                n1 += v
        for k, v in cnt2.items():
            if k in cnt1:
                n2 += v
        return [n1, n2]
