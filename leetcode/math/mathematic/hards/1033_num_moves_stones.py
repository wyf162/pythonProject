# _*_ coding: utf-8 _*_
# @Time : 2023/01/14 2:05 PM 
# @Author : yefe
# @File : 1033_num_moves_stones

from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = [a, b, c]
        stones.sort()
        mx = stones[-1] - stones[0] + 1 - 3
        mi = 1
        d1 = stones[1] - stones[0]
        d2 = stones[2] - stones[1]
        if d1 > 2 and d1 > 2:
            mi = 2
        if d1 == 1 and d2 == 1:
            mi = 0
        return [mi, mx]
