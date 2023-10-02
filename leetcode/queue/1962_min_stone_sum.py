# _*_ coding: utf-8 _*_
# @Time : 2022/05/03 4:08 AM 
# @Author : yefe
# @File : 1962_min_stone_sum
from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapify(piles)
        for _ in range(k):
            stone = heappop(piles)
            heappush(piles, stone//2)
        return sum(piles)*(-1)


if __name__ == '__main__':
    sol = Solution()
    piles = [5,4,9]
    k = 2
    ret = sol.minStoneSum(piles, k)
    print(ret)