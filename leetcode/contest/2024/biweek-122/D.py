# -*- coding : utf-8 -*-
# @Time: 2024/1/21 12:43
# @Author: yefei.wang
# @File: D.py

from typing import List

from sortedcontainers import SortedList


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        s = SortedList()
        res = nums[0]
        for i in range(1, 1 + dist + 1):
            s.add(nums[i])
        for i in range(k - 1):
            res += s[i]

        ans = res
        n = len(nums)
        for i in range(1, n - dist - 1):
            if k - 2 < len(s) and nums[i + dist + 1] < s[k - 2]:
                res += nums[i + dist + 1]
                res -= s[k - 2]
            s.add(nums[i + dist + 1])
            s.remove(nums[i])
            if k - 2 < len(s) and nums[i] < s[k - 2]:
                res -= nums[i]
                res += s[k - 2]
            ans = min(ans, res)
        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 3, 2, 6, 4, 2]
    # k = 3
    # dist = 3
    nums = [2, 6, 3, 8, 3, 1, 1]
    k = 3
    dist = 4
    ret = sol.minimumCost(nums, k, dist)
    print(ret)
