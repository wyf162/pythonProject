# -*- coding : utf-8 -*-
# @Time: 2024/6/8 22:32
# @Author: yefei.wang
# @File: D.py
from collections import defaultdict
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(k + 2)]
        mx = [0] * (k + 2)
        for x in nums:
            for i in range(k + 1, 0, -1):
                dp[i][x] = 1 + max(dp[i][x], mx[i - 1])
                mx[i] = max(mx[i], dp[i][x])
        return mx[k + 1]


if __name__ == '__main__':
    # nums = [1, 2, 1, 1, 3]
    # k = 2
    nums = [89, 89, 90, 88, 88, 88, 88, 90, 90]
    k = 2
    ret = Solution().maximumLength(nums, k)
    print(ret)
