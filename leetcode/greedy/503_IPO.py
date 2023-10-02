# _*_ coding: utf-8 _*_
# @Time : 2022/11/05 1:59 PM 
# @Author : yefe
# @File : 503_IPO

import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capitals: List[int]) -> int:
        nums = []
        for profit, capital in zip(profits, capitals):
            nums.append([capital, profit])
        nums.sort()

        q = []
        i = 0
        while k>0:
            while i<len(nums) and nums[i][0] <= w:
                heapq.heappush(q, -nums[i][1])
                i += 1
            if q:
                w -= heapq.heappop(q)
                k -= 1
            else:
                break
        return w


if __name__ == '__main__':
    sol = Solution()
    k = 2
    w = 0
    profits = [1, 2, 3]
    capitals = [0, 1, 1]
    ret = sol.findMaximizedCapital(k, w, profits, capitals)
    print(ret)
