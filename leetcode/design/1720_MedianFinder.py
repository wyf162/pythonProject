# -*- coding : utf-8 -*-
# @Time: 2022/8/8 20:46
# @Author: yefei.wang
# @File: 1720_MedianFinder.py

import heapq
# 小根堆


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:

        if self.right and num<self.right[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        while len(self.left)+1<len(self.right):
            num = heapq.heappop(self.right)
            heapq.heappush(self.left, -num)

        while len(self.right)+1<len(self.left):
            num = heapq.heappop(self.left)
            heapq.heappush(self.right, -num)

    def findMedian(self) -> float:
        if len(self.left)<len(self.right):
            return self.right[0]
        elif len(self.right)<len(self.left):
            return -self.left[0]
        else:
            return (-self.left[0]+self.right[0])/2


if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    ret = mf.findMedian()
    print(ret)
    mf.addNum(3)
    ret = mf.findMedian()
    print(ret)
    mf.addNum(3)
    ret = mf.findMedian()
    print(ret)