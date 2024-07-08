# -*- coding: utf-8 -*-
# @Time: 2024/7/8 13:06
# @Author: yfwang
# @File: 3209.py

from typing import List
from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        tot = 0
        dp = defaultdict(int)
        for num in nums:
            if num & k < k:
                dp = defaultdict(int)
                continue
            ndp = defaultdict(int)
            for k1, v1 in dp.items():
                if k1 & k < k:
                    continue
                elif k1 & num == k:
                    tot += v1
                    ndp[k1 & num] += v1
                else:
                    ndp[k1 & num] += v1
            if num == k:
                tot += 1
            ndp[num] += 1
            dp = ndp
        return tot


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 9, 9, 7, 4]
    k = 1
    ret = sol.countSubarrays(nums, k)
    print(ret)
