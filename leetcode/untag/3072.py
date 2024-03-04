# -*- coding: utf-8 -*-
# @Time: 2024/3/4 13:03
# @Author: yfwang
# @File: 3072.py
# https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii/description/

from typing import List
from sortedcontainers import SortedList


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        s1, s2 = SortedList(), SortedList()
        s1.add(nums[0])
        s2.add(nums[1])
        n = len(nums)
        idxs = [-1] * n
        idxs[0] = 1
        idxs[1] = 2
        for i in range(2, n):
            i1 = s1.bisect_right(nums[i])
            i2 = s2.bisect_right(nums[i])
            n1, n2 = len(s1), len(s2)
            if n1 - i1 > n2 - i2:
                s1.add(nums[i])
                idxs[i] = 1
            elif n1 - i1 < n2 - i2:
                s2.add(nums[i])
                idxs[i] = 2
            else:
                if n1 <= n2:
                    s1.add(nums[i])
                    idxs[i] = 1
                else:
                    s2.add(nums[i])
                    idxs[i] = 2
        ret1 = [x for i, x in enumerate(nums) if idxs[i] == 1]
        ret2 = [x for i, x in enumerate(nums) if idxs[i] == 2]
        rets = ret1 + ret2
        return rets


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 1, 3, 3]
    ret = sol.resultArray(nums)
    print(ret)
