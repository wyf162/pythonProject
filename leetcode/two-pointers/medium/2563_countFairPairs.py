# -*- coding : utf-8 -*-
# @Time: 2023/9/30 14:50
# @Author: yefei.wang
# @File: 2563_countFairPairs.py

import bisect

from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for j, num in enumerate(nums):
            left = bisect.bisect_left(nums, lower - num, 0, j)
            right = bisect.bisect_right(nums, upper - num, 0, j)
            ans += right - left
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 0, 0, 0, 0, 0]
    lower = 0
    upper = 0
    ret = sol.countFairPairs(nums, lower, upper)
    print(ret)
