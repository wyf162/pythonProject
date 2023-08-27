# _*_ coding: utf-8 _*_
# @Time : 2022/05/03 3:25 AM 
# @Author : yefe
# @File : 2163_minimum_difference
from heapq import heapify, heappushpop
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 3

        min_pq = nums[m - n:]
        heapify(min_pq)
        suf_max = [0] * (m - n + 1)  # 后缀最大和
        suf_max[-1] = s = sum(min_pq)
        for i in range(m - n - 1, n - 1, -1):
            s += nums[i] - heappushpop(min_pq, nums[i])
            suf_max[i] = s

        max_pq = [-v for v in nums[:n]]  # 所有元素取反当最大堆
        heapify(max_pq)
        pre_min = -sum(max_pq)  # 前缀最小和
        ans = pre_min - suf_max[n]
        for i in range(n, m - n):
            pre_min += nums[i] + heappushpop(max_pq, -nums[i])
            ans = min(ans, pre_min - suf_max[i + 1])
        return ans