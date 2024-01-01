# -*- coding : utf-8 -*-
# @Time: 2023/12/9 22:40
# @Author: yefei.wang
# @File: C.py
from collections import Counter
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        hst = Counter()
        ans = 0
        for j in range(n):
            hst[nums[j]] += 1
            if hst[nums[j]] > k:
                while i < n and hst[nums[j]] > k:
                    hst[nums[i]] -= 1
                    i += 1
            ans = max(ans, j - i + 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
