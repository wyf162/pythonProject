# -*- coding : utf-8 -*-
# @Time: 2024/5/5 10:43
# @Author: yefei.wang
# @File: D.py

from typing import List


class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        mod = 1000000007
        n = len(nums)
        mx = max(nums)
        diff = []
        for num in nums:
            diff.append(mx - num)
        mxd0 = max(diff)
        tot0 = sum(diff)
        ans = 1 << 64
        for y in range(0, mxd0 + 1, 1):
            mxd = mxd0 + y
            tot = tot0 + y * n
            if mxd * 2 < tot:
                ans = min(cost2 * (tot // 2) + cost1 * (tot - tot // 2 * 2), cost1 * tot, ans)
            else:
                ans = min(cost1 * tot, cost2 * (tot - mxd) + cost1 * (mxd * 2 - tot), ans)
        return ans % mod


if __name__ == '__main__':
    sol = Solution()
    # nums = [4, 1]
    # cost1 = 5
    # cost2 = 2
    nums = [3, 9, 1]
    cost1 = 5
    cost2 = 7
    ret = sol.minCostToEqualizeArray(nums, cost1, cost2)
    print(ret)
