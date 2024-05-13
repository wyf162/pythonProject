# _*_ coding: utf-8 _*_
# @Time : 2022/05/20 11:36 PM 
# @Author : yefe
# @File : 452_find_min_arrow_shots
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrow = None
        res = 0
        for s, t in points:
            if arrow is None:
                arrow = t
                res += 1
            else:
                if s <= arrow <= t:
                    continue
                else:
                    arrow = t
                    res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    # points = [[10,16],[2,8],[1,6],[7,12]]
    points = [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]
    ret = sol.findMinArrowShots(points)
    print(ret)
