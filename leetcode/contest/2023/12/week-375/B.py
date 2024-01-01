# -*- coding : utf-8 -*-
# @Time: 2023/12/10 10:33
# @Author: yefei.wang
# @File: B.py

from typing import List


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        n = len(variables)
        ans = []
        for i in range(n):
            a, b, c, m = variables[i]
            x = pow(a, b, 10)
            y = pow(x, c, m)
            if y == target:
                ans.append(i)
        return ans