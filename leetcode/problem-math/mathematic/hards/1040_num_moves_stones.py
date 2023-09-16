# _*_ coding: utf-8 _*_
# @Time : 2023/01/14 1:57 PM 
# @Author : yefe
# @File : 1040_num_moves_stones

from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        mx = stones[-1] - stones[0] + 1 - n
        mx -= min(stones[-1] - stones[-2] - 1, stones[1] - stones[0] - 1)
        i, j, mi = 0, 0, mx
        for i in range(n):
            while j + 1 < n and stones[j + 1] - stones[i] + 1 <= n:
                j += 1
            cost = n - (j - i + 1)
            if j - i + 1 == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                cost = 2
            mi = min(mi, cost)
        return [mi, mx]
