# _*_ coding: utf-8 _*_
# @Time : 2023/01/07 6:32 PM 
# @Author : yefe
# @File : 149_max_points

from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(m, n):
            return m if not n else gcd(n, m % n)

        def getslope(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]

            if dx == 0: return p1[0], 0
            if dy == 0: return 0, p1[1]

            d = gcd(dx, dy)
            return dx // d, dy // d

        res = 0
        for i in range(len(points)):
            d = defaultdict(lambda: 0)
            same, maxi = 1, 0
            p1 = points[i]
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p1 == p2:
                    same += 1
                else:
                    slope = getslope(p1, p2)
                    d[slope] += 1
                    maxi = max(maxi, d[slope])
            res = max(res, same + maxi)

        return res


if __name__ == '__main__':
    sol = Solution()
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    ret = sol.maxPoints(points)
    print(ret)
