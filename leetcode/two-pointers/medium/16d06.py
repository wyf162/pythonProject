# -*- coding : utf-8 -*-
# @Time: 2023/9/30 13:09
# @Author: yefei.wang
# @File: 16d06.py

from typing import List


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        i, j = 0, 0
        ans = 0xffffffff
        while i < len(a) and j < len(b):
            ans = min(ans, abs(a[i] - b[j]))
            if a[i] < a[j]:
                i += 1
            else:
                j += 1
        return ans