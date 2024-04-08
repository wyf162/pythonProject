# -*- coding: utf-8 -*-
# @Time: 2024/4/8 16:42
# @Author: yfwang
# @File: 2009.py
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        m = len(nums)
        i = 0
        ans = n
        for j in range(m):
            while nums[j] - nums[i] >= n:
                i += 1
            ans = min(ans, n - (j - i + 1))
        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums = [4, 2, 5, 3]
    nums = [1, 2, 3, 5, 6]
    ret = sol.minOperations(nums)
    print(ret)

