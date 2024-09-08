# -*- coding : utf-8 -*-
# @Time: 2024/9/8 10:33
# @Author: yefei.wang
# @File: B.py

from typing import List


class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        n = len(start)

        def check(x):
            low1, high1 = start[0], start[0] + d

            for i in range(1, n):
                low2, high2 = start[i], start[i] + d




