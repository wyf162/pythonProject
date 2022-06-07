# _*_ coding: utf-8 _*_
# @Time : 2022/06/07 8:26 PM 
# @Author : yefe
# @File : 875_min_eating_speed
import math
from bisect import bisect_left
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, 10 ** 9
        while l <= r:
            mid = (l + r) // 2
            if sum([math.ceil(pile / mid) for pile in piles]) <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l

    def minEatingSpeed2(self, piles: List[int], h: int) -> int:
        return bisect_left(range(max(piles)), -h, 1, key=lambda k: -sum((pile + k - 1) // k for pile in piles))


if __name__ == '__main__':
    sol = Solution()
    piles = [3, 6, 7, 11]
    h = 8
    ret = sol.minEatingSpeed(piles, h)
    print(ret)
