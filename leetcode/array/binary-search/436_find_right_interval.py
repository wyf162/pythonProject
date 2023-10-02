# _*_ coding: utf-8 _*_
# @Time : 2022/05/20 8:53 AM 
# @Author : yefe
# @File : 436_find_right_interval
from typing import List
import bisect


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        hst = dict()
        for i, interval in enumerate(intervals):
            hst[interval[0]] = i
        nums = sorted(list(hst.keys()))
        rets = list()
        for start, end in intervals:
            idx = bisect.bisect_left(nums, end)
            if idx<len(nums):
                rets.append(hst[nums[idx]])
            else:
                rets.append(-1)

        return rets


if __name__ == '__main__':
    sol = Solution()
    intervals = [[3, 4], [2, 3], [1, 2]]
    rets = sol.findRightInterval(intervals)
    print(rets)
