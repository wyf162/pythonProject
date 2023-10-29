# -*- coding : utf-8 -*-
# @Time: 2023/10/29 9:55
# @Author: yefei.wang
# @File: 274_hIndex.py
from typing import List
import bisect


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        l, r = 0, len(citations)
        ans = 0
        while l<=r:
            mid = (l+r)//2
            i = bisect.bisect_left(citations, mid)
            if n-i>mid:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
