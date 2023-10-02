# _*_ coding: utf-8 _*_
# @Time : 2022/05/19 12:25 AM 
# @Author : yefe
# @File : 46_permute
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        check = [0 for i in range(len(nums))]

        self.backtrack([], nums, check)
        return self.res

    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return

        for i in range(len(nums)):
            if check[i] == 0:
                check[i] = 1
                self.backtrack(sol + [nums[i]], nums, check)
                check[i] = 0


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    ret = sol.permute(nums)
    print(ret)
