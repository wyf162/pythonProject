# -*- coding : utf-8 -*-
# @Time: 2022/1/7 22:30
# @Author: yefei.wang
# @File: 220_contain_nearby_almost_duplicate.py
import collections
from typing import List
from sortedcontainers import SortedSet, SortedList
import bisect


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        ss = SortedList()
        n = len(nums)
        for i in range(n):
            if not ss:
                ss.add(nums[i])
            elif len(ss) < k:
                idx = bisect.bisect_left(ss, nums[i] - t)
                print(idx)
                if idx < len(ss) and ss[idx] <= nums[i] + t:
                    return True
                else:
                    ss.add(nums[i])
            else:
                idx = bisect.bisect_left(ss, nums[i] - t)
                print(idx)
                # print(ss[idx], nums[i]+t)
                if idx < len(ss) and ss[idx] <= nums[i] + t:
                    return True
                else:
                    ss.add(nums[i])
                ss.remove(nums[i-k])
            print(ss)
        return False


if __name__ == "__main__":
    nums = [1, 5, 9, 1, 5, 9]
    k = 2
    t = 3
    # nums = [1, 2, 3, 1]
    # k = 3
    # t = 0
    sol = Solution()
    data = sol.containsNearbyAlmostDuplicate(nums, k, t)
    print(data)
