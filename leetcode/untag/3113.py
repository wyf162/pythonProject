# -*- coding: utf-8 -*-
# @Time: 2024/4/16 17:15
# @Author: yfwang
# @File: 3113.py

from typing import List
from collections import Counter
from heapq import heappop, heappush


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        cnt = Counter()
        n = len(nums)
        h = []
        ans = 0
        for i, x in enumerate(nums):
            ans += cnt[x]
            while h and h[0] < x:
                y = heappop(h)
                cnt[y] -= 1
            heappush(h, x)
            cnt[x] += 1
        return ans + n


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 5, 4, 4]
    # nums = [9, 40, 40]
    ret = sol.numberOfSubarrays(nums)
    print(ret)
