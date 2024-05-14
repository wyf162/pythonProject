# -*- coding: utf-8 -*-
# @Time: 2024/5/14 13:12
# @Author: yfwang
# @File: 3143.py

from typing import List


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        nums = []
        n = len(points)
        for i in range(n):
            nums.append((max(abs(points[i][0]), abs(points[i][1])), i))
        nums.sort()

        td = 0x3f3f3f3f
        vis = set()
        for d, i in nums:
            if s[i] in vis:
                td = d
                break
            vis.add(s[i])
        ans = 0
        for d, i in nums:
            if abs(points[i][0]) < td and abs(points[i][1]) < td:
                ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    points = [[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]]
    s = "abdca"
    ret = sol.maxPointsInsideSquare(points, s)
    print(ret)
