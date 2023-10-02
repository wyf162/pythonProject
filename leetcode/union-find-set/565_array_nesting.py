# -*- coding : utf-8 -*-
# @Time: 2022/7/17 11:57
# @Author: yefei.wang
# @File: 565_array_nesting.py

from typing import List
from copy import deepcopy


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        unvis = [True] * n
        ans = 0
        for i, num in enumerate(nums):
            if unvis[i]:
                cur = i
                s = set()
                s.add(cur)
                unvis[cur] = False
                while nums[cur] not in s:
                    cur = nums[cur]
                    s.add(cur)
                    unvis[cur] = False
                ans = max(ans, len(s))
        return ans
