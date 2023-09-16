# _*_ coding: utf-8 _*_
# @Time : 2022/05/15 4:26 PM 
# @Author : yefe
# @File : 6066_count_intervals
from sortedcontainers import SortedSet, SortedList
from bisect import bisect_left, bisect_right


class CountIntervals2:
    def __init__(self, l=1, r=10 ** 9):
        self.left = self.right = None
        self.l, self.r, self.sum = l, r, 0

    def add(self, l: int, r: int) -> None:
        if self.sum == self.r - self.l + 1: return  # self 已被完整覆盖，无需执行任何操作
        if l <= self.l and self.r <= r:  # self 已被区间 [l,r] 完整覆盖，不再继续递归
            self.sum = self.r - self.l + 1  # 范围 [self.l,self.r] 内的所有整数都被区间覆盖
            return
        mid = (self.l + self.r) // 2
        if self.left is None: self.left = CountIntervals2(self.l, mid)  # 动态开点
        if self.right is None: self.right = CountIntervals2(mid + 1, self.r)  # 动态开点
        if l <= mid: self.left.add(l, r)
        if mid < r: self.right.add(l, r)
        self.sum = self.left.sum + self.right.sum

    def count(self) -> int:
        return self.sum


class CountIntervals:

    def __init__(self):
        self.ints = []
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        ints = self.ints
        lidx = bisect_left(ints, left, key=lambda itv:itv[1])
        ridx = bisect_right(ints, right, key=lambda itv:itv[0])

        for i in range(lidx, ridx):
            left = min(left, ints[lidx][0])
            right = max(right, ints[ridx-1][1])
            self.cnt -= ints[i][1]-ints[i][0]+1
        ints[lidx:ridx] = [(left, right)]
        self.cnt += right-left+1

    def count(self) -> int:
        return self.cnt


if __name__ == '__main__':

    count_intervals = CountIntervals()
    count_intervals.add(2, 3)
    count_intervals.add(7, 10)
    cnt = count_intervals.count()
    print(cnt)
    count_intervals.add(5, 8)
    cnt = count_intervals.count()
    print(cnt)

