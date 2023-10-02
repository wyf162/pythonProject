# _*_ coding: utf-8 _*_
# @Time : 2022/05/15 8:18 PM 
# @Author : yefe
# @File : 812_largest_triangle_area
import math
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    s = self.compute(points[i], points[j], points[k])
                    if s > res:
                        res = s
        return res

    @staticmethod
    def compute(x, y, z):
        a = math.sqrt((x[0] - y[0]) * (x[0] - y[0]) + (x[1] - y[1]) * (x[1] - y[1]))
        b = math.sqrt((x[0] - z[0]) * (x[0] - z[0]) + (x[1] - z[1]) * (x[1] - z[1]))
        c = math.sqrt((y[0] - z[0]) * (y[0] - z[0]) + (y[1] - z[1]) * (y[1] - z[1]))
        p = (a + b + c) / 2
        print(a, b, c, p)
        t = p * (p - a) * (p - b) * (p - c)
        if t > 0:
            s = math.sqrt(t)
            return s
        else:
            return 0


if __name__ == '__main__':
    sol = Solution()
    points = [[35, -23], [-12, -48], [-34, -40], [21, -25], [-35, -44], [24, 1], [16, -9], [41, 4], [-36, -49],
              [42, -49], [-37, -20], [-35, 11], [-2, -36], [18, 21], [18, 8], [-24, 14], [-23, -11], [-8, 44],
              [-19, -3], [0, -10], [-21, -4], [23, 18], [20, 11], [-42, 24], [6, -19]]
    ret = sol.largestTriangleArea(points)
    print(ret)
