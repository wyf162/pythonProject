# _*_ coding: utf-8 _*_
# @Time : 2023/03/05 5:52 PM 
# @Author : yefe
# @File : 6309_find_valid_split

from typing import List


class Solution:

    def findValidSplit(self, nums: List[int]):
        left = {}
        right = [0] * len(nums)

        def f(p: int, i: int) -> None:
            if p in left:
                right[left[p]] = i
            else:
                left[p] = i

        for i, x in enumerate(nums):
            d = 2
            while d*d <= x:
                if x%d == 0:
                    f(d, i)
                    x //=d
                    while x%d==0:
                        x //=d
                d += 1
            if x>1:
                f(x, i)

        max_r = 0
        for l, r in enumerate(right):
            if l>max_r:
                return max_r
            max_r = max(max_r, r)
        return -1
