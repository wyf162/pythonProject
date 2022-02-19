# -*- coding : utf-8 -*-
# @Time: 2022/2/14 20:50
# @Author: yefei.wang
# @File: 504_single_non_duplicate.py
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = len(nums)
        while l<r:
            m = (l+r)>>1
            if m%2==0:
                if nums[m]==nums[m-1]:
                    r = m
                elif m+1<n and nums[m]==nums[m+1]:
                    l = m-1
                else:
                    return nums[m]
            if m%2==1:
                if nums[m]==nums[m-1]:
                    l = m + 1
                elif m+1<n and nums[m]==nums[m+1]:
                    r = m
                else:
                    return nums[m]
        print(nums[l])
        return nums[l]

    def single_non_duplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid
        return nums[low]


if __name__ == '__main__':
    sol = Solution()
    # nums = [0,0,1,2,2,3,3,4,4,5,5,7,7]
    nums = [1,2,2]
    data = sol.singleNonDuplicate(nums)
    print(data)
