# -*- coding : utf-8 -*-
# @Time: 2022/1/26 21:30
# @Author: yefei.wang
# @File: 2013_detect_squares.py
import collections
import itertools
from typing import List


class DetectSquares:

    def __init__(self):
        self.points = dict()
        self.row = collections.defaultdict(set)
        self.col = collections.defaultdict(set)

    def add(self, point: List[int]) -> None:
        k = tuple(point)
        self.points[k] = self.points.get(k, 0) + 1
        x, y = point
        self.row[x].add(y)
        self.col[y].add(x)

    def count2(self, point: List[int]) -> int:
        ans = 0
        x, y = point
        for j, i in itertools.product(self.row.get(x, set()), self.col.get(y, set())):
            if self.points.get((i, j), 0):
                a = self.points.get((x, j), 0)
                b = self.points.get((i, y), 0)
                c = self.points.get((i, j), 0)
                ans += a * b * c
        return ans

    def count(self, point: List[int]) -> int:
        ans = 0
        x, y = point
        for i in self.col.get(y, set()):
            l = abs(x - i)
            if l == 0:
                continue
            if y - l in self.row.get(x, set()) and self.points.get((i, y - l)):
                a = self.points.get((x, j), 0)
                b = self.points.get((i, y), 0)
                c = self.points.get((i, j), 0)
                ans += a * b * c
            if y + l in self.row.get(x, set()) and self.points.get((i, y + l)):
                a = self.points.get((x, j), 0)
                b = self.points.get((i, y), 0)
                c = self.points.get((i, j), 0)
                ans += a * b * c
        return ans


if __name__ == '__main__':
    dt = DetectSquares()
    for point in [[3, 10], [11, 2], [3, 2]]:
        dt.add(point)
    data = dt.count([11, 10])
    print(data)
