# _*_ coding: utf-8 _*_
# @Time : 2022/4/22 下午7:35 
# @Author : wangyefei
# @File : 396_max_rotate_function.py
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = sum([i*num for i,num in enumerate(nums)])
        s = sum(nums)
        for i in range(1, n):
            dp[i] = dp[i-1]+s-n*nums[n-i]
        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    nums = [4,3,2,6]
    ret = sol.maxRotateFunction(nums)
    print(ret)