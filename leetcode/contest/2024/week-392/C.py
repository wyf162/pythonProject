# -*- coding : utf-8 -*-
# @Time: 2024/4/7 10:29
# @Author: yefei.wang
# @File: C.py
import bisect
from typing import List


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        mid = n // 2
        if nums[mid] < k:
            idx = 0
            for i in range(mid, n):
                if nums[i] < k:
                    i += 1
                    idx = i
                else:
                    break
            ans = k * (idx - mid) - sum(nums[mid:idx])
        elif nums[mid] > k:
            idx = 0
            for i in range(n):
                if nums[i] <= k:
                    i += 1
                    idx = i
                else:
                    break
            ans = sum(nums[idx:mid + 1]) - k * (mid - idx + 1)
        else:
            ans = 0
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 5, 6, 8, 5]
    k = 7
    ret = sol.minOperationsToMakeMedianK(nums, k)
    print(ret)
