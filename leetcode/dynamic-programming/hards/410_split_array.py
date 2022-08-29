# _*_ coding: utf-8 _*_
# @Time : 2022/08/26 9:23 PM 
# @Author : yefe
# @File : 410_split_array

from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        M = 0x3f3f3f3f
        n = len(nums)
        dp = [[M for j in range(m+1)] for i in range(n+1)]

        pres = [0]*(n+1)
        for i in range(n):
            pres[i+1] = pres[i] + nums[i]

        dp[0][0] = 0

        for i in range(1, n+1):
            for j in range(1, min(m+1, i+1)):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], pres[i]-pres[k]))

        return dp[n][m]


if __name__ == '__main__':
    sol = Solution()
    nums = [7,2,5,10,8]
    m = 2
    ret = sol.splitArray(nums, m)
    print(ret)
