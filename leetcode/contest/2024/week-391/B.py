# -*- coding : utf-8 -*-
# @Time: 2024/3/31 10:29
# @Author: yefei.wang
# @File: B.py

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        x = numBottles
        y = numExchange
        while x >= y:
            ans += 1
            x -= y
            y += 1
            x += 1
        return ans
