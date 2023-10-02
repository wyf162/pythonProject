# _*_ coding: utf-8 _*_
# @Time : 2022/05/22 3:39 PM 
# @Author : yefe
# @File : 496_next_greater_element
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        hst = {}
        stk = []
        for i in range(n-1, -1, -1):
            while stk and nums2[stk[-1]]<=nums2[i]:
                stk.pop()
            if stk:
                hst[nums2[i]] = nums2[stk[-1]]
            else:
                hst[nums2[i]] = -1
            stk.append(i)

        rets = [-1]*len(nums1)
        for i, num in enumerate(nums1):
            rets[i] = hst[num]
        return rets


if __name__ == '__main__':
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    rets = Solution().nextGreaterElement(nums1, nums2)
    print(rets)
