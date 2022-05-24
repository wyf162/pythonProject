# _*_ coding: utf-8 _*_
# @Time : 2022/05/24 8:30 AM 
# @Author : yefe
# @File : 295_MedianFinder
import bisect

from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        self.c = SortedList()

    def addNum(self, num: int) -> None:
        # idx = bisect.bisect_left(self.c, num)
        # self.c.insert(idx, num)
        self.c.add(num)

    def findMedian(self) -> float:
        n = len(self.c)
        m = n >> 1
        if n % 2 == 1:
            return self.c[m]
        else:
            return (self.c[m] + self.c[m - 1]) / 2


if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    ret = mf.findMedian()
    print(ret)
    mf.addNum(3)
    mf.addNum(4)
    mf.addNum(5)
    mf.addNum(6)

    ret = mf.findMedian()
    print(ret)
