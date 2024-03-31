# -*- coding : utf-8 -*-
# @Time: 2024/3/31 10:29
# @Author: yefei.wang
# @File: A.py

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        d = sum(int(c) for c in str(x))
        if x % d == 0:
            return d
        else:
            return -1
