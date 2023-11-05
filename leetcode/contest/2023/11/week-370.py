# -*- coding : utf-8 -*-
# @Time: 2023/11/5 10:30
# @Author: yefei.wang
# @File: week-370.py
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


class Solution:

    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        b = [x - i for i, x in enumerate(nums)]
        sb = sorted(b)
        v2i = dict()
        i = 0
        for x in sb:
            if x in v2i:
                continue
            else:
                v2i[x] = i
                i += 1

        seg_tree = SegmentTree([0] * i)

        dp = [x for x in nums]
        dp[0] = nums[0]
        if dp[0] > 0:
            seg_tree.update(v2i[b[0]], dp[0], 0, 0, seg_tree.n - 1)
        for i in range(1, n):
            mx = seg_tree.query(0, v2i[b[i]], 0, 0, seg_tree.n - 1)
            dp[i] = max(dp[i], mx + nums[i])
            if dp[i] > 0:
                seg_tree.update(v2i[b[i]], dp[i], 0, 0, seg_tree.n - 1)
        rst = max(dp)
        return rst


if __name__ == '__main__':
    sol = Solution()
    # nums = [3, 3, 5, 6]
    # nums = [5, -1, -3, 8]
    # nums = [-2,-1]
    # nums = [2, 7]
    # nums = [-9, -5, 2, 2, 7]
    nums = [7, 7, -8, -6, -1, 4, 9, -7, 8, -3]
    ret = sol.maxBalancedSubsequenceSum(nums)
    print(ret)
