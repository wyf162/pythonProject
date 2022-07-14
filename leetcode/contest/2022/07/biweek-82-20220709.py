# -*- coding : utf-8 -*-
# @Time: 2022/7/9 22:53
# @Author: yefei.wang
# @File: biweek-82-20220709.py


from bisect import bisect_right
from functools import reduce
from typing import List
import copy


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        passengers.sort()
        buses.sort()
        n = len(buses)
        cur = 0
        for i in range(n):
            if i != n - 1:
                time = buses[i]
                b = bisect_right(passengers, time)

                if b - cur < capacity:
                    cur = b
                else:
                    cur += capacity
            if i == n - 1:
                time = buses[i]
                b = bisect_right(passengers, time)
                if b - cur < capacity:
                    lst = passengers[cur:b]
                else:
                    lst = passengers[cur:cur + capacity]
        if not lst or len(lst) < capacity and lst[-1] < buses[-1]:
            return buses[-1]
        res = lst[-1]
        total = set(passengers)
        for i in range(res - 1, -1, -1):
            if i not in total:
                return i

    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        dl = []
        for x, y in zip(nums1, nums2):
            dl.append(abs(x - y))
        dl.sort()
        k1 += k2
        tot = sum(dl)
        if k1 >= tot:
            return 0
        l, r = 0, dl[-1]
        while l < r:
            mid = (l + r + 1) // 2
            tmp = 0
            for x in dl:
                if x > mid:
                    tmp += x - mid
            if tmp >= k1:
                l = mid
            else:
                r = mid - 1
        tmp = 0
        ans = 0
        for x in dl:
            if x > l:
                tmp += x - l
                ans += l * l
            else:
                ans += x * x

        tmp -= k1
        ans += tmp * (l * 2 + 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 4, 10, 12]
    nums2 = [5, 8, 6, 9]
    k1 = 1
    k2 = 3
    # nums1 = [1, 2, 3, 4]
    # nums2 = [2, 10, 20, 19]
    # k1 = 0
    # k2 = 0
    ret = sol.minSumSquareDiff(nums1, nums2, k1, k2)
    print(ret)
