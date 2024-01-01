# -*- coding : utf-8 -*-
# @Time: 2023/12/10 10:36
# @Author: yefei.wang
# @File: C.py

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        idxs = []
        ans = 0
        for i, x in enumerate(nums):
            if x == mx:
                idxs.append(i)
            if len(idxs) >= k:
                ans += idxs[-k] + 1
        return ans


