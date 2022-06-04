# -*- coding : utf-8 -*-
# @Time: 2021/12/9 0:50
# @Author: yefei.wang
# @File: 689_maxSumOfThreeSubarrays.py

from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp0 = [0] * (n + 1)
        s = sum(nums[0:k])
        dp0[k] = s
        dp1 = [0] * (n + 1)
        fp1 = [0] * (n + 1)
        dp1[k] = s
        fp1[k] = 0
        for i in range(1, n - k + 1):
            s = s - nums[i - 1] + nums[i + k - 1]
            dp0[i + k] = s
            if dp1[i + k - 1] < s:
                dp1[i + k] = s
                fp1[i + k] = i
            else:
                dp1[i + k] = dp1[i + k - 1]
                fp1[i + k] = fp1[i + k - 1]
        # print(dp0)
        # print('dp1', dp1)
        # print('fp1', fp1)

        s = sum(nums[0:k * 2])
        dp2 = [0] * (n + 1)
        fp2 = [[] for _ in range(n + 1)]
        dp2[0 + k * 2] = s
        fp2[0 + k * 2] = [0, k]
        for i in range(1, n - k * 2 + 1):
            if dp0[i + k * 2] + dp1[i + k] > dp2[i + k * 2 - 1]:
                dp2[i + k * 2] = dp0[i + k * 2] + dp1[i + k]
                fp2[i + k * 2] = [fp1[i + k], i + k]
            else:
                dp2[i + k * 2] = dp2[i + k * 2 - 1]
                fp2[i + k * 2] = fp2[i + k * 2 - 1]
        # print('dp2', dp2)
        # print('fp2', fp2)

        s = sum(nums[0:k*3])
        dp3 = [0]*(n+1)
        fp3 = [[] for _ in range(n+1)]
        dp3[0+k*3] = s
        fp3[0+k*3] = [0,k,k*2]
        for i in range(1,n-k*3+1):
            if dp0[i+k*3]+dp2[i+k*2] > dp3[i+k*3-1]:
                dp3[i+k*3] = dp0[i+k*3]+dp2[i+k*2]
                fp3[i+k*3] = [fp2[i+k*2][0], fp2[i+k*2][1], i+k*2]
            else:
                dp3[i+k*3] = dp3[i+k*3-1]
                fp3[i+k*3] = fp3[i+k*3-1]
        # print('dp3', dp3)
        # print('fp3', fp3)

        return fp3[-1]

