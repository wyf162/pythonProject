# -*- coding : utf-8 -*-
# @Time: 2024/4/28 10:33
# @Author: yefei.wang
# @File: B.py

from typing import List


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        n1 = len(nums1)
        n2 = len(nums2)
        ans = 2000
        for i1 in range(n1):
            for i2 in range(i1 + 1, n1):

                diffs = []
                j1 = 0
                for j2 in range(n2):
                    while j1 in (i1, i2):
                        j1 += 1
                    diff = nums2[j2] - nums2[j1]
                    j1 += 1
                    if diffs:
                        if diffs[-1] != diff:
                            diffs.append(diff)
                            break
                    else:
                        diffs.append(diff)
                if len(diffs) == 1:
                    ans = min(ans, diffs[0])
        return ans
