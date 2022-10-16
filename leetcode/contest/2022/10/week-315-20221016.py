# _*_ coding: utf-8 _*_
# @Time : 2022/10/16 10:44 AM 
# @Author : yefe
# @File : week-315-20221016

from typing import List
from math import comb


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        cnt = 0

        if minK == maxK:
            t = 0
            for num in nums:
                if num == minK:
                    t += 1
                else:
                    cnt += comb(t, 2) + t
                    t = 0
            cnt += comb(t, 2) + t
            return cnt
        else:
            valid_min = 0
            valid_max = 0
            for i, num in enumerate(nums):
                if num == minK:
                    valid_min += 1
                    cnt += valid_max
                elif num < minK:
                    valid_min = 0
                    valid_max = 0

                if num == maxK:
                    valid_max += 1
                    cnt += valid_min
                elif num > maxK:
                    valid_max = 0
                    valid_min = 0

                if minK < num < maxK:
                    cnt += valid_max * valid_min
                print(cnt)
            return cnt


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 3, 5, 2, 7, 5]
    # minK = 1
    # maxK = 5
    # nums = [1, 2, 1, 1]
    # minK = 1
    # maxK = 1
    nums = [35054, 398719, 945315, 945315, 820417, 945315, 35054, 945315, 171832, 945315, 35054, 109750, 790964, 441974,
            552913]
    minK = 35054
    maxK = 945315
    ret = sol.countSubarrays(nums, minK, maxK)
    print(ret)
