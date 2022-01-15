# -*- coding : utf-8 -*-
# @Time: 2022/1/12 22:14
# @Author: yefei.wang
# @File: 10_dynamic_programming.py

class Solution:
    def translateNum(self, num: int) -> int:
        nums = list(str(num))
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, n):
            if nums[i - 1] == '1' or (nums[i - 1] == '2' and nums[i] < '7'):
                if nums[i - 2] == '1' or (nums[i - 2] == '2' and nums[i-1] < '7'):
                    dp[i + 1] = max(dp[i-1]+4, dp[i]+2)
                else:
                    dp[i + 1] = max(dp[i-1]+2, dp[i]+1)
            else:
                dp[i + 1] = dp[i]
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    num = 111111
    res = sol.translateNum(num)
    print(res)
