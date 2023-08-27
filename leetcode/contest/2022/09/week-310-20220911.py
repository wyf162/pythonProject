# _*_ coding: utf-8 _*_
# @Time : 2022/09/11 10:31 AM 
# @Author : yefe
# @File : week-210-20220911

from collections import Counter, defaultdict
from typing import List
from sortedcontainers import SortedDict


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

    def change(self, index: int, val: int, node: int, s: int, e: int):
        if s == e:
            self.seg[node] = val
            return
        m = s + (e - s) // 2
        if index <= m:
            self.change(index, val, node * 2 + 1, s, m)
        else:
            self.change(index, val, node * 2 + 2, m + 1, e)
        self.seg[node] = max(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def range(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:
            return self.seg[node]
        m = s + (e - s) // 2
        if right <= m:
            return self.range(left, right, node * 2 + 1, s, m)
        if left > m:
            return self.range(left, right, node * 2 + 2, m + 1, e)
        return max(self.range(left, m, node * 2 + 1, s, m), self.range(m + 1, right, node * 2 + 2, m + 1, e))


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hst = defaultdict(int)
        for num in nums:
            if num % 2 == 0:
                hst[num] += 1
        if not hst:
            return -1

        ans_k, ans_v = None, None
        for k, v in hst.items():
            if ans_k is None:
                ans_k = k
                ans_v = v
            elif v > ans_v:
                ans_k = k
                ans_v = v
            elif v == ans_v and k < ans_k:
                ans_k = k

        return ans_k

    def partitionString(self, s: str) -> int:
        i = 0
        vis = set()
        res = 1
        while i < len(s):
            if s[i] not in vis:
                vis.add(s[i])
                i += 1
            else:
                res += 1
                vis = set()
                vis.add(s[i])
                i += 1
        return res

    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        hst = defaultdict(int)

        for left, right in intervals:
            hst[left] += 1
            hst[right + 1] -= 1

        res = 0

        pres = 0
        for k in sorted(hst.keys()):
            pres += hst[k]
            res = max(res, pres)
        return res

    def lengthOfLIS(self, nums: List[int], k: int) -> int:

        seg_tree = SegmentTree([0]*100007)

        hst = SortedDict()

        for num in nums:
            if num not in hst:
                hst[num] = 1
            cnt = seg_tree.range(max(num-k, 0), num-1, 0, 0, 100001)
            if cnt + 1 > hst[num]:
                hst[num] = cnt + 1

            seg_tree.change(num, hst[num], 0, 0, 100001)

        # print(hst)
        return max(hst.values())


if __name__ == '__main__':
    sol = Solution()

    nums = [4, 2, 1, 4, 3, 4, 5, 8, 15]
    k = 3

    ret = sol.lengthOfLIS(nums, k)
    print(ret)

    # intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
    # intervals = [[1, 2], [3, 3], [3, 4]]
    # ret = sol.minGroups(intervals)
    # print(ret)

    # s = "hdklqkcssgxlvehva"
    # ret = sol.partitionString(s)
    # print(ret)
