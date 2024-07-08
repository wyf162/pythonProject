# -*- coding: utf-8 -*-
# @Time: 2024/7/8 13:59
# @Author: yfwang
# @File: 3202.py

from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        f = [[0] * k for _ in range(k)]
        for x in nums:
            x %= k
            for y, fxy in enumerate(f[x]):
                f[y][x] = fxy + 1
        return max(map(max, f))




if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    k = 2
    ret = sol.maximumLength(nums, k)
    print(ret)
