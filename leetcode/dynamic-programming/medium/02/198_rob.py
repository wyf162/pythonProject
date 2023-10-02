# -*- coding : utf-8 -*-
# @Time: 2023/9/16 11:20
# @Author: yefei.wang
# @File: 198_rob.py

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0 for _ in range(n)]
        f[0] = nums[0]
        f[1] = nums[1]
        for i in range(2, n):
            for j in range(i-1):
                f[i] = max(f[i], f[j] + nums[i])
        return f[-1]
