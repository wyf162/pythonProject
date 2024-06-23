# -*- coding : utf-8 -*-
# @Time: 2024/6/23 10:29
# @Author: yefei.wang
# @File: C.py

from functools import cache
from typing import List


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return nums[0] + abs(nums[1])
            else:
                return max(dfs(i - 1) + nums[i], dfs(i - 2) + nums[i - 1] - nums[i])

        ans = dfs(n - 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, -2, 3, 4]
    nums = [1, -2, -3]
    nums = [1, -1, 1, -1]
    nums = [0]
    ret = sol.maximumTotalCost(nums)
    print(ret)
