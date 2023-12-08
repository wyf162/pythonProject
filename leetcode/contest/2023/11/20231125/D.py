# -*- coding : utf-8 -*-
# @Time: 2023/11/25 22:28
# @Author: yefei.wang
# @File: D.py

from typing import List
from bisect import bisect_left
from heapq import heappop, heappush


class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        dp = [dict() for i in range(n)]
        for i in range(n):
            dp[i][1] = pre_sum[i + 1]

        for i in range(n):
            k = max(dp[i].keys())
            v = dp[i][k]
            ij = bisect_left(pre_sum, pre_sum[i + 1] + v)
            for j in range(ij, min(ij + 10, n + 1)):
                # if j < n and pre_sum[j] - pre_sum[i + 1] > nums[j]:
                #     break
                if k + 1 not in dp[j-1]:
                    dp[j - 1][k + 1] = pre_sum[j] - pre_sum[i + 1]
                else:
                    dp[j - 1][k + 1] = min(dp[j - 1][k + 1], pre_sum[j] - pre_sum[i + 1])
        rst = max(dp[-1].keys())
        return rst


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 2, 3, 4]
    # nums = [4, 3, 2, 6]
    # nums = [5, 2, 2]
    # nums = [272, 482, 115, 925, 983]
    # nums = [417, 241, 895, 308, 259, 562]
    nums = [8, 938, 879, 679, 132, 301, 992, 983, 196, 361, 981, 356]
    ret = sol.findMaximumLength(nums)
    print(ret)
