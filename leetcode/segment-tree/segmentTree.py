# _*_ coding: utf-8 _*_
# @Time : 2022/4/4 下午8:01 
# @Author : wangyefei
# @File : segmentTree.py
from typing import List


class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.seg = [0] * (n * 4)
        self.build(nums, 0, 0, n - 1)

    def build(self, nums: List[int], node: int, s: int, e: int):
        if s == e:
            self.seg[node] = nums[s]
            return
        m = s + (e - s) // 2
        self.build(nums, node * 2 + 1, s, m)
        self.build(nums, node * 2 + 2, m + 1, e)
        self.seg[node] = self.seg[node * 2 + 1] + self.seg[node * 2 + 2]

    def change(self, index: int, val: int, node: int, s: int, e: int):
        if s == e:
            self.seg[node] = val
            return
        m = s + (e - s) // 2
        if index <= m:
            self.change(index, val, node * 2 + 1, s, m)
        else:
            self.change(index, val, node * 2 + 2, m + 1, e)
        self.seg[node] = self.seg[node * 2 + 1] + self.seg[node * 2 + 2]

    def range(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:
            return self.seg[node]
        m = s + (e - s) // 2
        if right <= m:
            return self.range(left, right, node * 2 + 1, s, m)
        if left > m:
            return self.range(left, right, node * 2 + 2, m + 1, e)
        return self.range(left, m, node * 2 + 1, s, m) + self.range(m + 1, right, node * 2 + 2, m + 1, e)


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        segment_tree = SegmentTree(nums)
        ret = 0
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                if lower<=segment_tree.range(i,j,0,0,n-1)<=upper:
                    ret += 1
        return ret


if __name__ == '__main__':
    sol = Solution()
    nums = [-2, 5, -1]
    lower = -2
    upper = 2
    ret = sol.countRangeSum(nums, lower, upper)
    print(ret)

