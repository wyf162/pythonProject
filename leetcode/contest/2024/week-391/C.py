# -*- coding : utf-8 -*-
# @Time: 2024/3/31 10:29
# @Author: yefei.wang
# @File: C.py

from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        cur = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                cur += 1
            else:
                arr.append(cur)
                cur = 1
        arr.append(cur)
        ans = 0
        for x in arr:
            ans += x * (x + 1) // 2
        return ans
