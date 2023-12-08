# -*- coding : utf-8 -*-
# @Time: 2023/10/12 22:24
# @Author: yefei.wang
# @File: segmentTree.py
from typing import List


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


class SegmentTreeMax:
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
        self.seg[node] = max(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def update(self, index: int, val: int, node: int, s: int, e: int):
        if s == e:
            self.seg[node] = val
            return
        m = s + (e - s) // 2
        if index <= m:
            self.update(index, val, node * 2 + 1, s, m)
        else:
            self.update(index, val, node * 2 + 2, m + 1, e)
        self.seg[node] = max(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def query(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:
            return self.seg[node]
        m = s + (e - s) // 2
        if right <= m:
            return self.query(left, right, node * 2 + 1, s, m)
        if left > m:
            return self.query(left, right, node * 2 + 2, m + 1, e)
        return max(self.query(left, m, node * 2 + 1, s, m), self.query(m + 1, right, node * 2 + 2, m + 1, e))
