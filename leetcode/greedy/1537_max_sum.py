# -*- coding : utf-8 -*-
# @Time: 2022/8/7 19:09
# @Author: yefei.wang
# @File: 1537_max_sum.py

from typing import List


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        hst1 = {val: idx for idx, val in enumerate(nums1)}
        hst2 = {val: idx for idx, val in enumerate(nums2)}

        sames = []
        for num in nums1:
            if num in hst2:
                sames.append(num)

        pres1 = [0]
        for num in nums1:
            pres1.append(pres1[-1] + num)

        pres2 = [0]
        for num in nums2:
            pres2.append(pres2[-1] + num)

        if not sames:
            return max(pres1[-1], pres2[-1])
        else:
            idx1 = 0
            idx2 = 0
            ans = 0
            for same in sames:
                ans += max(pres1[hst1[same]] - pres1[idx1], pres2[hst2[same]] - pres2[idx2])
                idx1 = hst1[same]
                idx2 = hst2[same]
            ans += max(pres1[-1]-pres1[idx1], pres2[-1]-pres2[idx2])
            return ans


if __name__ == '__main__':
    sol = Solution()
    nums1 = [2, 4, 5, 8, 10]
    nums2 = [4, 6, 8, 9]
    ret = sol.maxSum(nums1, nums2)
    print(ret)
