# _*_ coding: utf-8 _*_
# @Time : 2022/4/5 下午1:24 
# @Author : wangyefei
# @File : 17016_massage.py
from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    nums = [2,1,1,2]
    ret = sol.massage(nums)
    print(ret)
