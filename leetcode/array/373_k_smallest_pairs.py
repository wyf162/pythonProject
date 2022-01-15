# -*- coding : utf-8 -*-
# @Time: 2022/1/14 18:57
# @Author: yefei.wang
# @File: 373_k_smallest_pairs.py
import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        flag, ans = (m := len(nums1)) > (n := len(nums2)), list()
        if flag:
            m, n, nums1, nums2 = n, m, nums2, nums1
        pq = []
        for i in range(min(m, k)):
            heapq.heappush(pq, (nums1[i] + nums2[0], i, 0))
        while len(ans) < k and pq:
            _, a, b = heapq.heappop(pq)
            ans.append([nums2[b], nums1[a]] if flag else [nums1[a], nums2[b]])
            if b + 1 < n:
                heapq.heappush(pq, (nums1[a] + nums2[b + 1], a, b + 1))
        return ans


if __name__ == '__main__':
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 10
    sol = Solution()
    ans = sol.kSmallestPairs(nums1, nums2, k)
    print(ans)
