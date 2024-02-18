# -*- coding : utf-8 -*-
# @Time: 2024/2/18 10:28
# @Author: yefei.wang
# @File: B.py

from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = [str(x) for x in arr1]
        arr2 = [str(x) for x in arr2]
        hst = set()
        for s1 in arr1:
            for i in range(len(s1)):
                hst.add(s1[:i+1])

        ans = 0
        for s2 in arr2:
            for i in range(len(s2)):
                t2 = s2[:i+1]
                if t2 in hst:
                    ans = max(ans, i+1)
        return ans
