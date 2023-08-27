# _*_ coding: utf-8 _*_
# @Time : 2022/10/22 2:18 PM 
# @Author : yefe
# @File : 1235_job_scheduling

from typing import List
from collections import defaultdict


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0


class SegmentTree:

    def __init__(self):
        self.root = Node()
        self.n = 10 ** 9

    def update(self, node, start, end, l, r, val):
        if l <= start and end <= r:
            node.val = val
            return
        self.push_down(node)
        mid = (start + end) >> 1
        if l <= mid:
            self.update(node.left, start, mid, l, r, val)
        if r > mid:
            self.update(node.right, mid + 1, end, l, r, val)
        self.push_up(node)

    def query(self, node, start, end, l, r):
        if l <= start and end <= r:
            return node.val
        self.push_down(node)
        mid = (start + end) >> 1
        ans = 0
        if l <= mid:
            ans = self.query(node.left, start, mid, l, r)
        if r > mid:
            ans = max(ans, self.query(node.right, mid + 1, end, l, r))
        return ans

    @staticmethod
    def push_down(node):
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()

    @staticmethod
    def push_up(node):
        node.val = max(node.left.val, node.right.val)


class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profits: List[int]) -> int:
        sg = SegmentTree()
        hst = defaultdict(list)
        for start, end, profit in zip(startTime, endTime, profits):
            hst[end].append((start, profit))

        dp = defaultdict(int)

        for end in sorted(hst.keys()):
            for start, profit in hst[end]:
                dp[end] = max(dp[end], sg.query(sg.root, 0, sg.n, 0, start) + profit)
            sg.update(sg.root, 0, sg.n, end, end, dp[end])

        return max(dp.values())


if __name__ == '__main__':
    sol = Solution()
    # startTime = [1, 2, 3, 3]
    # endTime = [3, 4, 5, 6]
    # profit = [50, 10, 40, 70]
    startTime = [1, 2, 3, 4, 6]
    endTime = [3, 5, 10, 6, 9]
    profits = [20, 20, 100, 70, 60]
    ret = sol.jobScheduling(startTime, endTime, profits)
    print(ret)
