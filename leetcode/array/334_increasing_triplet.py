# -*- coding : utf-8 -*-
# @Time: 2022/1/12 21:42
# @Author: yefei.wang
# @File: 334_increasing_triplet.py
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = nums[0]
        second = None
        for num in nums:
            if second and num > second:
                return True
            if num > first:
                second = num
            elif num < first:
                first = num

        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 0, -1, 0, 1]
    data = sol.increasingTriplet(nums)
    print(data)
