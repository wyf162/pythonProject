# -*- coding : utf-8 -*-
# @Time: 2023/11/19 10:30
# @Author: yefei.wang
# @File: week-372.py

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
        self.seg[node] = min(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def update(self, index: int, val: int, node: int, s: int, e: int):
        if s == e:
            self.seg[node] = val
            return
        m = s + (e - s) // 2
        if index <= m:
            self.update(index, val, node * 2 + 1, s, m)
        else:
            self.update(index, val, node * 2 + 2, m + 1, e)
        self.seg[node] = min(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def query(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:
            return self.seg[node]
        m = s + (e - s) // 2
        if right <= m:
            return self.query(left, right, node * 2 + 1, s, m)
        if left > m:
            return self.query(left, right, node * 2 + 2, m + 1, e)
        return min(self.query(left, m, node * 2 + 1, s, m), self.query(m + 1, right, node * 2 + 2, m + 1, e))


class Solution:

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        m = len(heights)
        hs = dict()
        for i, h in enumerate(sorted(set(heights))):
            hs[h] = i + 1
        # print(hs)
        MN = 10 ** 5 + 5
        nums = [MN] * (len(hs) + 5)

        ans = [-1] * n

        g = [[] for i in range(m)]
        for j in range(n):
            mx, mi = max(queries[j]), min(queries[j])
            g[mx].append([mi, j])

        sg = SegmentTree(nums)
        for i in range(m - 1, -1, -1):
            sg.update(hs[heights[i]], i, 0, 0, sg.n - 1)
            if i + 1 < m:
                for mi, j in g[i]:
                    mx_h = max(hs[heights[i]], hs[heights[mi]]) + 1
                    ti = sg.query(mx_h, sg.n - 1, 0, 0, sg.n - 1)
                    ans[j] = ti if ti < 10 ** 5 + 5 else -1

            for mi, j in g[i]:
                if i == mi:
                    ans[j] = i
                elif heights[mi] < heights[i]:
                    ans[j] = i
        return ans


if __name__ == '__main__':
    sol = Solution()
    # heights = [6, 4, 8, 5, 2, 7]
    # queries = [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
    # heights = [5, 3, 8, 2, 6, 1, 4, 6]
    # queries = [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]
    # heights = [1, 2, 1, 2, 1, 2]
    # queries = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 0],
    #            [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 0], [4, 1],
    #            [4, 2], [4, 3], [4, 4], [4, 5], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
    heights = [380706162, 152637541, 853364690]
    queries = [[1, 0], [1, 1], [1, 0], [0, 1], [0, 1], [2, 0], [1, 1], [0, 2], [1, 2], [0, 2]]
    ret = sol.leftmostBuildingQueries(heights, queries)
    print(ret)

    # a = 0
    # b = 3
    # n = 1
    # ret = sol.maximumXorProduct(a, b, n)
    # print(ret)

    # s = '0011'
    # ret = sol.minimumSteps(s)
    # print(ret)

# [1, 2, 1, 2, 1, 2]
# [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 0], [2, 1], [2, 2],
#  [2, 3], [2, 4], [2, 5], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5],
#  [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
# [0, 1, 3, 3, 5, 5, 1, 1, -1, -1, -1, -1, 3, -1, 2, 3, 5, 5, 3, -1, 3, 3, -1, -1, 5, -1, 5, -1, 4, 5, 5, -1, 5, -1, 5, 5]
