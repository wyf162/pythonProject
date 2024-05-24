# -*- coding : utf-8 -*-
# @Time: 2022/6/18 19:03
# @Author: yefei.wang
# @File: 698_can_partition_k_subsets.py
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s_num = sum(nums)
        if s_num % k:
            return False
        part_sum = s_num // k
        n = len(nums)
        dp = [-1] * (1 << n)
        dp[0] = 0
        for s in range(1, 1 << n):
            for idx, num in enumerate(nums):
                if s & (1 << idx) == 0:
                    continue
                else:
                    s1 = s & ~(1 << idx)
                    if dp[s1] >= 0 and dp[s1] + num <= part_sum:
                        dp[s] = (dp[s1] + num) % part_sum
                        break
        return dp[-1] == 0


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    ret = sol.canPartitionKSubsets(nums, k)
    print(ret)
