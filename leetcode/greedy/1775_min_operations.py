# _*_ coding: utf-8 _*_
# @Time : 2022/12/07 9:41 PM 
# @Author : yefe
# @File : 1775_min_operations

from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        n1, n2 = len(nums1), len(nums2)
        l1, r1 = 0, len(nums1) - 1
        l2, r2 = 0, len(nums2) - 1
        s1 = sum(nums1)
        s2 = sum(nums2)
        if n1 * 6 < n2 or n2 * 6 < n1:
            return -1
        d = abs(s1 - s2)
        ans = 0
        while d > 0:
            d1 = abs(nums1[l1] - nums2[r2])
            d2 = abs(nums1[r1] - nums2[l2])
            if d1 < d2:
                d -= d2
                r1 -= 1
                l2 += 1
            else:
                d -= d1
                r2 -= 1
                l1 += 1
            ans += 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums1 = [1, 2, 3, 4, 5, 6]
    # nums2 = [1, 1, 2, 2, 2, 2]
    nums1 = [6, 6]
    nums2 = [1]
    ret = sol.minOperations(nums1, nums2)
    print(ret)
