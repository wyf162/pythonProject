# _*_ coding: utf-8 _*_
# @Time : 2022/05/15 7:36 PM 
# @Author : yefe
# @File : 715_range
import bisect


class RangeModule:
    def __init__(self):
        self.range = []

    def addRange(self, left: int, right: int) -> None:
        first = bisect.bisect_left(self.range, left, key=lambda r: r[1])
        last = bisect.bisect_right(self.range, right, key=lambda r: r[0]) # not included
        if first < last:
            left = min(left, self.range[first][0])
            right = max(right, self.range[last-1][1])
            self.range = self.range[:first] + [[left, right]] + self.range[last:]
        else:
            self.range.insert(first, [left, right])

    def queryRange(self, left: int, right: int) -> bool:
        idx = bisect.bisect_right(self.range, left, key=lambda r: r[0]) - 1
        return 0 <= idx < len(self.range) and self.range[idx][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        first = bisect.bisect_right(self.range, left, key=lambda r: r[1])
        last = bisect.bisect_left(self.range, right, key=lambda r: r[0]) # not included
        if first < last:
            r = []
            if self.range[first][0] < left:
                r.append([self.range[first][0], left])
            if self.range[last-1][1] > right:
                r.append([right, self.range[last-1][1]])
            self.range = self.range[:first] + r + self.range[last:]
