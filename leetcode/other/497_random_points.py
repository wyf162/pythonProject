# _*_ coding: utf-8 _*_
# @Time : 2022//24 8:03 PM 
# @Author : yefe
# @File : 497_random_points
import random
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        n = 0
        for rect in rects:
            ai, bi, xi, yi = rect
            n += (xi - ai + 1) * (yi - bi + 1)
        self.rects = rects

    def pick(self) -> List[int]:
        cursor = 0
        ret = []
        for rect in self.rects:
            ai, bi, xi, yi = rect
            for i in range(ai, xi + 1):
                for j in range(bi, yi + 1):
                    cursor += 1
                    if random.randrange(cursor) == 0:
                        ret = [i, j]
        return ret


if __name__ == '__main__':
    rects = [[-2, -2, -1, -1], [1, 0, 3, 0]]
    sol = Solution(rects)
    ret = sol.pick()
    print(ret)
    ret = sol.pick()
    print(ret)
    ret = sol.pick()
    print(ret)
    ret = sol.pick()
    print(ret)
