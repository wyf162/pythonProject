# _*_ coding: utf-8 _*_
# @Time : 2022/05/19 12:34 AM 
# @Author : yefe
# @File : 47_permute_unique
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]

        self.backtrack([], nums, check)
        return self.res

    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return

        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol + [nums[i]], nums, check)
            check[i] = 0


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 2]
    ret = sol.permuteUnique(nums)
    print(ret)