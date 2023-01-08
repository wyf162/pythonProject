# _*_ coding: utf-8 _*_
# @Time : 2023/01/07 4:08 PM 
# @Author : yefe
# @File : 1658_min_operations

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        left = 0
        s = 0
        ans = -1
        for idx, num in enumerate(nums):
            s += num
            while s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, idx - left + 1)
        return len(nums)-ans if ans > 0 else -1


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 4, 2, 3]
    x = 5
    ret = sol.minOperations(nums, x)
    print(ret)
