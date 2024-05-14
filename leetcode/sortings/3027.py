# -*- coding: utf-8 -*-
# @Time: 2024/3/8 13:52
# @Author: yfwang
# @File: 3027.py

from math import inf
from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        ans = 0
        for i, (_, y0) in enumerate(points):
            max_y = -inf
            for (_, y) in points[i + 1:]:
                if max_y < y <= y0:
                    max_y = y
                    ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    # points = [[6, 2], [4, 4], [2, 6]]
    points = [[0, 3], [5, 4], [6, 2]]
    ret = sol.numberOfPairs(points)
    print(ret)
