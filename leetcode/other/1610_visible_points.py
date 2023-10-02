# -*- coding : utf-8 -*-
# @Time: 2021/12/16 21:21
# @Author: yefei.wang
# @File: 1610_visible_points.py
from typing import List
import math
import bisect
from math import atan2, pi

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        tmp = 0
        angles = list()
        for point in points:
            t_angle = self.convert(location, point)
            if  t_angle is None:
                tmp += 1
            else:
                angles.append(t_angle)
        angles.sort()
        print(len(angles), angles)
        ans = 0
        n = len(angles)
        stk = list()
        for i in range(2*n):
            print(i)
            if not stk:
                stk.append((i,angles[i%n]))
            else:
                while stk and self.compute(stk[0][1],angles[i%n])>angle:
                    stk.pop(0)
                if stk and stk[0][0]==i%n:
                    print("break")
                    break
                stk.append((i,angles[i%n]))
            ans = max(ans, len(stk))
            print(stk)
        return ans+tmp

    def convert(self, observer, point):
        x1,y1 = observer
        x2,y2 = point
        if x1==x2 and y1==y2:
            angle=None
        if x1==x2:
            if y2>y1:
                angle = 90
            elif y1>y2:
                angle = 270
        elif y1==y2:
            if x2>x1:
                angle = 0
            else:
                angle = 180
        else:
            if x2>x1 and y2>y1:
                angle = 180 * math.atan(abs((y2 - y1) / (x2 - x1))) / math.pi
            elif x2<x1 and y2>y1:
                angle = 180 * math.atan(abs((x2 - x1)/(y2 - y1))) / math.pi
                angle = abs(angle)+90
            elif x2<x1 and y2<y1:
                angle = 180 * math.atan(abs((y2 - y1) / (x2 - x1))) / math.pi
                angle = abs(angle)+180
            else:
                angle = 180 * math.atan(abs((x2 - x1)/(y2 - y1))) / math.pi
                angle = abs(angle)+270

        return angle


    def compute(self, x, y):
        if y>=x:
            return y-x
        else:
            return 360-x+y


class SolutionLeetCode:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        sameCnt = 0
        polarDegrees = []
        for p in points:
            if p == location:
                sameCnt += 1
            else:
                polarDegrees.append(atan2(p[1] - location[1], p[0] - location[0]))
        polarDegrees.sort()
        print(polarDegrees)

        n = len(polarDegrees)
        polarDegrees += [deg + 2 * pi for deg in polarDegrees]
        print(polarDegrees)

        maxCnt = 0
        right = 0
        degree = angle * pi / 180
        for i in range(n):
            while right < n * 2 and polarDegrees[right] <= polarDegrees[i] + degree:
                right += 1
            print(right, i)
            maxCnt = max(maxCnt, right - i)
        return sameCnt + maxCnt


if __name__ == "__main__":
    sol = Solution()
    print(sol.compute(318,0))
    points = [[1,1],[2,2],[3,3],[4,4],[1,2],[2,1]]
    angle = 0
    location = [1,1]

    # points = [[30, 48], [26, 26], [82, 91], [63, 7], [3, 65], [74, 0], [12, 26], [12, 46], [57, 1], [32, 17], [96, 37], [21, 54],
    #  [20, 47], [88, 61], [88, 44], [69, 18], [21, 50], [23, 42], [48, 43], [9, 93], [45, 81], [43, 58], [14, 82],
    #  [92, 63], [16, 33], [49, 34], [57, 50], [59, 91], [59, 61], [13, 80], [21, 81], [3, 56], [30, 85], [70, 94],
    #  [59, 27], [56, 15], [4, 50], [30, 11], [45, 82], [87, 49], [12, 24], [93, 37], [20, 38], [53, 76], [28, 25],
    #  [65, 93], [31, 86], [25, 50], [63, 60], [79, 48], [73, 58], [76, 63], [99, 43], [17, 45], [53, 9], [99, 38],
    #  [10, 31], [14, 22], [30, 53], [34, 88], [37, 59], [66, 86], [87, 58], [100, 15], [48, 0], [55, 31], [50, 19],
    #  [96, 32], [40, 79], [46, 45], [73, 47], [74, 28], [72, 66], [35, 42], [6, 89], [62, 49], [67, 42], [80, 47],
    #  [82, 31], [8, 96], [97, 59], [36, 65], [31, 48], [69, 11], [12, 25], [68, 56], [39, 62], [37, 8], [58, 36],
    #  [5, 56], [99, 94], [80, 94], [64, 70], [80, 61], [76, 47], [78, 67], [41, 70], [85, 60], [15, 40], [40, 50],
    #  [20, 44], [87, 32], [55, 90], [33, 76], [76, 65], [49, 50], [51, 10], [70, 76], [1, 28]]
    # angle = 180
    # location = [52, 19]
    # points = [[60, 61], [58, 47], [17, 26], [87, 97], [63, 63], [26, 50], [70, 21], [3, 89], [51, 24], [55, 14], [6, 51],
    #  [64, 21], [66, 33], [54, 35], [87, 38], [30, 0], [37, 92], [92, 12], [60, 73], [75, 98], [1, 11], [88, 24],
    #  [82, 92]]
    # angle = 44
    # location = [15, 50]

    print(sol.visiblePoints(points, angle, location))


    # points = [[1, 0], [2, 1]]
    # angle = 13
    # location = [1, 1]
    # print(sol.visiblePoints(points, angle, location))
    #
    # sol.convert(location,[1,0])
    # sol.convert(location, [2, 1])
    #
    #
    # points = [[2, 1], [2, 2], [3, 4], [1, 1]]
    # angle = 90
    # location = [1, 1]
    # print(sol.visiblePoints(points, angle, location))

    points = [[0,0], [math.cos(pi/4), math.sin(pi/4)],
              [math.cos(3 * pi / 4), math.sin(3 * pi / 4)],
              [math.cos(5 * pi / 4), math.sin(5 * pi / 4)],
              [math.cos(7* pi / 4), math.sin(7 * pi / 4)]]
    for point in points:
        angle = sol.convert([0, 0],point)
        print(angle)

    points = [[0,0], [math.cos(pi/6), math.sin(pi/6)],
              [math.cos(4 * pi / 6), math.sin(4 * pi / 6)],
              [math.cos(7 * pi / 6), math.sin(7 * pi / 6)],
              [math.cos(10 * pi / 6), math.sin(10 * pi / 6)]]
    for point in points:
        angle = sol.convert([0, 0],point)
        print(angle)