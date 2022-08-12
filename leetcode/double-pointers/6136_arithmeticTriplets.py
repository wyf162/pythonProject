# -*- coding : utf-8 -*-
# @Time: 2022/8/7 15:23
# @Author: yefei.wang
# @File: 6136_arithmeticTriplets.py
from typing import List


class Solution:

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans, i, j = 0, 0, 1
        for x in nums:
            while nums[j] + diff < x:
                j += 1
            if nums[j] + diff > x:
                continue
            while nums[i] + diff * 2 < x:
                i += 1
            if nums[i] + diff * 2 == x:
                ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 1, 4, 6, 7, 10]
    diff = 3
    ret = sol.arithmeticTriplets(nums, diff)
    print(ret)
