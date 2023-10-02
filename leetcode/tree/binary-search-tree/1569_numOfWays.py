# -*- coding : utf-8 -*-
# @Time: 2023/10/2 12:37
# @Author: yefei.wang
# @File: 1569_numOfWays.py
import math
from typing import List



class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        def dfs(nums):
            if len(nums) < 1:
                return 1
            small, large = [], []
            for i in range(1, len(nums), 1):
                if nums[i] > nums[0]:
                    large.append(nums[i])
                else:
                    small.append(nums[i])
            x, y = len(large), len(small)
            fx = dfs(large)
            fy = dfs(small)
            return math.comb(x+y, x) * fx % MOD * fy % MOD

        rst = dfs(nums) - 1
        rst %= MOD
        return rst


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 4, 5, 1, 2]
    ret = sol.numOfWays(nums)
    print(ret)
