# -*- coding : utf-8 -*-
# @Time: 2023/9/30 17:01
# @Author: yefei.wang
# @File: 1498_numSubseq.py

import bisect

from typing import List

module = 10 ** 9 + 7


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        k = bisect.bisect_right(nums, target >> 1)
        ans = 0
        for left in range(min(k+1, n)):
            right = bisect.bisect_right(nums, target - nums[left])
            if right > left:
                ans += 1 << (right - left - 1)
                ans %= module

        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [5, 2, 4, 1, 7, 6, 8]
    target = 16
    ret = sol.numSubseq(nums, target)
    print(ret)
