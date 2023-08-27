# _*_ coding: utf-8 _*_
# @Time : 2023/03/06 10:35 PM 
# @Author : yefe
# @File : 2585_ways_to_reach_target

from typing import List


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        f = [1] + [0] * target
        for count, marks in types:
            for j in range(target, 0, -1):
                for k in range(1, min(count, j // marks) + 1):
                    f[j] += f[j - k * marks]
                f[j] %= MOD
        return f[-1]
