# -*- coding : utf-8 -*-
# @Time: 2024/6/16 10:29
# @Author: yefei.wang
# @File: D.py

from typing import List


class FenwickTree:
    """
    Reference: https://en.wikipedia.org/wiki/Fenwick_tree
    https://github.com/atcoder/ac-library/blob/master/document_en/fenwicktree.md
    """

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: int) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> int:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> int:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        fwt = FenwickTree(n)
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                fwt.add(i, 1)

        rets = []
        for qry in queries:
            if qry[0] == 1:
                if qry[2] - qry[1] < 1:
                    rets.append(0)
                else:
                    ret = fwt.sum(qry[1] + 1, qry[2])
                    rets.append(ret)
            elif qry[0] == 2:
                idx, val = qry[1:]
                if idx - 2 >= 0 and idx < n:
                    if nums[idx - 2] < nums[idx - 1] > nums[idx]:
                        fwt.add(idx - 1, -1)
                    if nums[idx - 2] < nums[idx - 1] > val:
                        fwt.add(idx - 1, 1)

                if idx - 1 >= 0 and idx + 1 < n:
                    if nums[idx - 1] < nums[idx] > nums[idx + 1]:
                        fwt.add(idx, -1)
                    if nums[idx - 1] < val > nums[idx + 1]:
                        fwt.add(idx, 1)

                if idx >= 0 and idx + 2 < len(nums):
                    if nums[idx] < nums[idx + 1] > nums[idx + 2]:
                        fwt.add(idx + 1, -1)
                    if val < nums[idx + 1] > nums[idx + 2]:
                        fwt.add(idx + 1, 1)
                nums[idx] = val
        return rets


if __name__ == '__main__':
    sol = Solution()
    # nums = [3, 1, 4, 2, 5]
    # queries = [[2, 3, 4], [1, 0, 4]]
    nums = [4, 1, 4, 2, 1, 5]
    queries = [[2, 2, 4], [1, 0, 2], [1, 0, 4]]
    rets = sol.countOfPeaks(nums, queries)
    print(rets)
