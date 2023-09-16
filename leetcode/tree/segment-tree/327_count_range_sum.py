# _*_ coding: utf-8 _*_
# @Time : 2022/05/15 4:30 PM 
# @Author : yefe
# @File : 327_count_range_sum
from typing import List


class SegTree:  # 线段树，数组实现
    def __init__(self, n):
        self.n = n
        self.treesum = [0 for _ in range(4 * self.n)]

    def update(self, ID, diff):
        self._update(0, 0, self.n - 1, ID, diff)

    def query(self, ql, qr):
        return self._query(0, 0, self.n - 1, ql, qr)

    def _update(self, root, l, r, ID, diff):
        if l == r == ID:
            self.treesum[root] += diff
            return
        left = 2 * root + 1
        right = 2 * root + 2
        mid = l + r >> 1
        if ID <= mid:
            self._update(left, l, mid, ID, diff)
        else:
            self._update(right, mid + 1, r, ID, diff)
        self.treesum[root] = self.treesum[left] + self.treesum[right]

    def _query(self, root, l, r, ql, qr):
        if l == ql and r == qr:
            return self.treesum[root]
        left = 2 * root + 1
        right = 2 * root + 2
        mid = l + r >> 1
        if qr <= mid:
            return self._query(left, l, mid, ql, qr)
        elif mid + 1 <= ql:
            return self._query(right, mid + 1, r, ql, qr)
        else:
            return self._query(left, l, mid, ql, mid) + self._query(right, mid + 1, r, mid + 1, qr)


class Solution:

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n1 = len(nums)
        presum = [0 for _ in range(n1 + 1)]
        for i in range(n1):
            presum[i + 1] = presum[i] + nums[i]
        # ------------------列举所有数字 去重 排序 离散化
        all_num = []
        for p in presum:
            all_num += [p, p - lower, p - upper]
        all_num = list(set(all_num))
        all_num.sort()
        n2 = len(all_num)
        val_id = dict()
        for i, val in enumerate(all_num):
            val_id[val] = i

        res = 0
        ST = SegTree(n2)
        for p in presum:
            L = val_id[p - upper]
            R = val_id[p - lower]
            res += ST.query(L, R)

            ST.update(val_id[p], 1)

        return res
