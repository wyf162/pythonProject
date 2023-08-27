# _*_ coding: utf-8 _*_
# @Time : 2023/01/23 4:12 PM 
# @Author : yefe
# @File : 2542_max_score

import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = [[y, x] for x, y in zip(nums1, nums2)]
        nums.sort(key=lambda x: (-x[0], x[1]))

        m = nums[k-1][0]
        p = [_[1] for _ in nums[:k]]
        heapq.heapify(p)
        s = sum(p)
        ans = m*s

        for i in range(k, len(nums)):
            m = nums[i][0]
            x = nums[i][1]
            if x <= p[0]:
                continue
            else:
                y = heapq.heappop(p)
                s = s - y + x
                heapq.heappush(p, x)
                ans = max(ans, m*s)
        return ans
