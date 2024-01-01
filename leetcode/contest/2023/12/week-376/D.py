# -*- coding : utf-8 -*-
# @Time: 2023/12/17 10:57
# @Author: yefei.wang
# @File: D.py

import bisect

from typing import List


class Solution:
    def maxFrequencyScore(self, nums: List[int], K: int) -> int:
        n = len(nums)
        nums.sort()
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        def check(k):
            rst = 0x3f3f3f3f3f3f
            for i in range(k, n + 1):
                j = i - k
                mid = (nums[(i + j) // 2] + nums[(i + j - 1) // 2]) // 2
                j1 = bisect.bisect_left(nums, mid)
                cost1 = mid * (j1 - i) - (pre_sum[j1] - pre_sum[i])
                cost2 = (pre_sum[j] - pre_sum[j1]) - mid * (j - j1)
                cost = cost1 + cost2
                rst = min(rst, cost)
            return rst

        l, r = 1, n
        ans = 1
        while l <= r:
            m = (l + r) >> 1
            ret = check(m)
            print(m, ret)
            if ret <= K:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 2, 6, 4]
    # k = 3
    nums = [1, 4, 4, 2, 4]
    k = 0
    ret = sol.maxFrequencyScore(nums, k)
    print(ret)
