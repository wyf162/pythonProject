# _*_ coding: utf-8 _*_
# @Time : 2022/05/24 8:17 AM 
# @Author : yefe
# @File : 315_count_smaller
import bisect
from typing import List

from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sl = SortedList()
        rets = [0]*n
        for i in range(n-1, -1, -1):
            if not sl:
                rets[i]=0
                sl.add(nums[i])
            else:
                idx = bisect.bisect_left(sl, nums[i])
                rets[i] = idx
                sl.add(nums[i])
        return rets


if __name__ == '__main__':
    nums = [5,2,3,2,6,1]
    rets = Solution().countSmaller(nums)
    print(rets)