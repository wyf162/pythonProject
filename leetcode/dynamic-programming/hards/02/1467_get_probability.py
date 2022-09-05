# _*_ coding: utf-8 _*_
# @Time : 2022/09/03 2:50 PM 
# @Author : yefe
# @File : 1467_get_probability

from functools import cache
from typing import List
from math import comb


class Solution:
    def getProbability(self, balls: List[int]) -> float:

        s = sum(balls)
        l = len(balls)

        @cache
        def dfs(i, c, t):
            if i == l:
                return int(t == 0 and c == s // 2)
            res = dfs(i + 1, c, t + 1) + + dfs(i + 1, c + balls[i], t - 1)
            for j in range(1, balls[i]):
                res += dfs(i + 1, c + j, t) * comb(balls[i], j)
            return res

        res = dfs(0, 0, 0)
        return res / comb(s, s // 2)


if __name__ == '__main__':
    sol = Solution()
    balls = [2, 2, 2]
    ret = sol.getProbability(balls)
    print(ret)
