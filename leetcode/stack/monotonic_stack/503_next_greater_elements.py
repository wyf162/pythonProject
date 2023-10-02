# _*_ coding: utf-8 _*_
# @Time : 2022/05/22 3:48 PM 
# @Author : yefe
# @File : 503_next_greater_elements
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums.extend(nums)

        n = len(nums)
        rets = [-1] * n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] <= nums[i]:
                stk.pop()
            if stk:
                rets[i] = nums[stk[-1]]
            stk.append(i)
        return rets[:n >> 1]


if __name__ == '__main__':
    nums = [1, 2, 1]
    ret = Solution().nextGreaterElements(nums)
    print(ret)
